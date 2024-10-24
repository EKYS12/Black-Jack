'''
This file contains the game logic for Black Jack.
'''

from deck import Deck
from player import Player
import game_functions

import sys

print('Welcome to Black Jack')

print('Would you like to play?')

print('\n1. Yes, start a game')
print('\n2. No, exit')

not_valid_input = True

while not_valid_input:
    user_input = int(input('Choice: '))

    if user_input in [1,2]:
        not_valid_input = False

    else:
        print('Invalid input, try again')

if user_input == 1:

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

if user_input == 2:
    sys.exit()


