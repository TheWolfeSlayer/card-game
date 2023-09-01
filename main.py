import pygame
import random

pygame.init()

class Card():
  def __init__(self, value, suit):
    self.value = value
    # Sets value of face cards
    if value == 1:
      self.value = 'Ace'
    elif value == 11:
      self.value = 'Jack'
    elif value == 12:
      self.value = 'Queen'
    elif value == 13:
      self.value = 'King'
      
    self.suit = suit

    self.image = f'./cards/card-{suit.lower()}-{value}.png'
    
    # Adds a color value to the card depending on suit
    if suit == 'Hearts' or suit == 'Diamonds':
      self.color = 'Red'
    if suit == 'Clubs' or suit == 'Spades':
      self.color = 'Black'

  #prints the value of the card
  def printCard(self):
    print(self.value, 'of' , self.suit)

# Makes a user with a name and starting money
class User():
  def __init__(self, name, money):
    self.name = name
    self.money = money

def get_card(deckOfCards):
  temp_deck = deckOfCards
  # Gets a random card out of the deck and assigns it a variable
  rand_card = random.choice(temp_deck)
  # Removes the card from the deck to prevent duplicates
  temp_deck.remove(rand_card)
  # Returns the random card selected
  return pygame.transform.rotozoom(pygame.image.load(rand_card.image), 0, 3), rand_card

def start_game():
  deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
  new_user.money -= 2
  # Gets 6 random cards from temp deck
  first_hidden_card = get_card(deck)
  second_hidden_card = get_card(deck)
  third_hidden_card = get_card(deck)
  first_visible_card = get_card(deck)
  second_visible_card = get_card(deck)
  third_visible_card = get_card(deck)
  print('got all cards')

  return first_visible_card, first_hidden_card, second_visible_card, second_hidden_card, third_visible_card, third_hidden_card

def test_card(visible_card, hidden_card):
  # If cards share the same color and number
  if visible_card.value == hidden_card.value and visible_card.color == hidden_card.color:
    new_user.money += 20
    compare_message = f'Cards are the same color and suit(+$20), player now has {new_user.money}'
  # If cards share the same number
  elif visible_card.value == hidden_card.value:
    new_user.money += 10
    compare_message = f'Cards are the same number(+$10), player now has {new_user.money}'
  # If cards share the same suit
  elif visible_card.suit == hidden_card.suit:
    new_user.money += 5
    compare_message = f'Cards are the same suit(+$5), player now has {new_user.money}'
  # If cards share the same color
  elif visible_card.color == hidden_card.color:
    new_user.money += 1
    compare_message = f'Cards are the same color($+1), player now has {new_user.money}'
  # If there is nothing in common between the two cards
  else:
    compare_message = f'You won nothing! You still have {new_user.money}'
  return font.render(compare_message, True, (0,0,0), text_bg)

font = pygame.font.Font('freesansbold.ttf', 32)

def load_cards():
  WIN.blit(back_card,(first_hidden_loc))
  WIN.blit(back_card,(second_hidden_loc))
  WIN.blit(back_card,(third_hidden_loc))
  WIN.blit(user_cards[0][0],(first_card_loc))
  WIN.blit(user_cards[2][0],(second_card_loc))
  WIN.blit(user_cards[4][0],(third_card_loc))


suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fun card game")

CARD_SIZE = 96,144
Scale = 3
Scaled_card_size = CARD_SIZE[0] * Scale, CARD_SIZE[1] * Scale
first_card_loc = 0,0
second_card_loc = 375,0
third_card_loc = 750,0
first_hidden_loc = first_card_loc[0] + 60, first_card_loc[1] + 50
second_hidden_loc = second_card_loc[0] + 60, second_card_loc[1] + 50
third_hidden_loc = third_card_loc[0] + 60, third_card_loc[1] + 50
text_loc = 20, HEIGHT - 100
text_bg = pygame.Color("skyblue")

global result
welcome_message = 'Welcome to my game, you will be starting with $500', 'It takes $2 to play the game, click a card to start'
result = font.render(welcome_message[0], True, (0,0,0), text_bg)

new_user = User('User', 500)

back_card = pygame.transform.rotozoom(pygame.image.load('./cards/card-back1.png'), 0, 3)
user_cards=start_game()



while True:
  
  first_card = pygame.Rect(first_card_loc, Scaled_card_size)
  second_card = pygame.Rect(second_card_loc, Scaled_card_size)
  third_card = pygame.Rect(third_card_loc, Scaled_card_size)
  WIN.fill("white")
  text_box = pygame.Rect((0, HEIGHT-150), (WIDTH, 150))
  pygame.draw.rect(WIN, text_bg, text_box)
  load_cards()
  WIN.blit(result,(text_loc))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      # Set the x, y postions of the mouse click
      x, y = event.pos
        
      if text_box.collidepoint(x, y):
        result = font.render(welcome_message[1], True, (0,0,0), text_bg)
      elif first_card.collidepoint(x, y):
        result = test_card(user_cards[0][1], user_cards[1][1])
        user_cards=start_game()
      elif second_card.collidepoint(x, y):
        result = test_card(user_cards[2][1], user_cards[3][1])
        user_cards=start_game()
      elif third_card.collidepoint(x, y):
        result = test_card(user_cards[4][1], user_cards[5][1])
        user_cards=start_game()
      else:
        print('invalid click')
      
  
  pygame.display.flip()
