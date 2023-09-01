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
    self.back = '.cards/card-back1.png'
    
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
  # Gets a random card out of the deck and assigns it a variable
  rand_card = random.choice(deckOfCards)
  # Removes the card from the deck to prevent duplicates
  deckOfCards.remove(rand_card)
  # Returns the random card selected
  return rand_card

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
# Makes base deck
base_deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

card = pygame.image.load(base_deck[0].image)

first_card = pygame.image.load(get_card(base_deck).image)

pygame.init()
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fun card game")

while True:
  temp_deck = base_deck

  WIN.fill("white")
  WIN.blit(first_card,(0,0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
  pygame.display.update()