import pygame
import random

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
  return pygame.image.load(rand_card.image), rand_card

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
  print(f'Comparing {visible_card.value} of {visible_card.suit} with {hidden_card.value} of {hidden_card.suit}')
  # If cards share the same color and number
  if visible_card.value == hidden_card.value and visible_card.color == hidden_card.color:
    new_user.money += 20
    print(f'Cards are the same color and suit(+$20), player now has {new_user.money}')
  # If cards share the same number
  elif visible_card.value == hidden_card.value:
    new_user.money += 10
    print(f'Cards are the same number(+$10), player now has {new_user.money}')
  # If cards share the same suit
  elif visible_card.suit == hidden_card.suit:
    new_user.money += 5
    print(f'Cards are the same suit(+$5), player now has {new_user.money}')
  # If cards share the same color
  elif visible_card.color == hidden_card.color:
    new_user.money += 1
    print(f'Cards are the same color($+1), player now has {new_user.money}')
  # If there is nothing in common between the two cards
  else:
    print(f'You won nothing! You still have {new_user.money}')


suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fun card game")

CARD_SIZE = 96,144
first_card_loc = 0,0
second_card_loc = 150,0
third_card_loc = 300,0

new_user = User('Math', 500)

back_card = pygame.image.load('./cards/card-back1.png')
user_cards=start_game()

while True:
  pygame.init()
  first_card = pygame.Rect(first_card_loc, CARD_SIZE)
  second_card = pygame.Rect(second_card_loc, CARD_SIZE)
  third_card = pygame.Rect(third_card_loc, CARD_SIZE)
  WIN.fill("white")
  WIN.blit(back_card,(30,20))
  WIN.blit(user_cards[0][0],(first_card_loc))
  WIN.blit(back_card,(180, 20))
  WIN.blit(user_cards[2][0],(second_card_loc))
  WIN.blit(back_card,(330, 20))
  WIN.blit(user_cards[4][0],(third_card_loc))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      # Set the x, y postions of the mouse click
      x, y = event.pos
      
      if first_card.collidepoint(x, y):
        test_card(user_cards[0][1], user_cards[1][1])
      elif second_card.collidepoint(x, y):
        test_card(user_cards[2][1], user_cards[3][1])
      elif third_card.collidepoint(x, y):
        test_card(user_cards[4][1], user_cards[5][1])
      else:
        print('invalid click')
      user_cards=start_game()
  
  pygame.display.update()
