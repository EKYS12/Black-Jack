'''
This file contains the game logic for Black Jack.
'''

from deck import Deck
from player import Player
import game_functions as gf

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
    gf.game_setup(players, deck)
    
    gf.game_status(players, player_titles)
    
    for i, player_title in enumerate(player_titles):
        turn = True
    
        while turn:
            print()
            print(player_title)
            print(players[i])
            player_choice = gf.player_turn(player_title)
    
            if player_choice == 1:
                gf.hit(players[i], deck)
                print(players[i])
    
                if gf.check_bust(players[i]):
                    turn = False
                    players[i].bust = True
                    print(f'\n{player_title} has busted')
    
            else:
                turn = False
                print(f'\n{player_title} has chosen to stand with {gf.count_hand(players[i])} points.')

    winners = []
    busted = []
    max_points = 0

    for i, player_title in enumerate(player_titles):

        if players[i].bust == False:
            if gf.count_hand(players[i]) > max_points:
                winners = [player_title]
                max_count = gf.count_hand(players[i])
            elif gf.count_hand(players[i]) == max_points:
                winners.append(player_title)

        else:
            busted.append(player_title)

    print(f'{winners} won the game. {busted}  busted.')

if user_input == 2:
    sys.exit()


