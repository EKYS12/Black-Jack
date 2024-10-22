'''
This file contains the game logic for Black Jack.
'''

from deck import Deck
from player import Player
import game_functions

# Start of Game

# Create Dealer
dealer = Player(dealer=True)

# Create Players
player1 = Player()

player2 = Player()

# Group players and dealer in a list
players = [player1, player2, dealer]
player_titles = ['Player 1', 'Player 2', 'Dealer']

# Create Deck and shuffle
deck = Deck()

deck.shuffle()

# Set up the game
game_functions.game_setup(players, deck)

game_functions.game_status(players, player_titles)
