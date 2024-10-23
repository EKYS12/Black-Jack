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

for i, player_title in enumerate(player_titles):
    turn = True

    while turn:
        print()
        print(player_title)
        print(players[i])
        player_choice = game_functions.player_turn(player_title)

        if player_choice == 1:
            game_functions.hit(players[i], deck)
            print(players[i])

            if game_functions.check_bust(players[i]):
                turn = False
                print(f'\n{player_title} has busted')

        else:
            turn = False
            print(f'\n{player_title} has chosen to stand with {game_functions.count_hand(players[i])} points.')
