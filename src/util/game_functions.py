from deck import Deck
from player import Player

def hit(player, deck, hidden=False):
    '''
    Function for the act of "hitting" in Black Jack, where the player will draw a card and add it to their hand.

    player: Player that is hitting.

    deck: Deck that is being drawn from.

    hidden: Default=False; Determines if a card should be hidden information for the table.
    '''

    card = deck.draw()

    if hidden:
        # hide_card(card)
        return

    player.hand.append(card)

    return

def stand(player):
    '''
    Function for the act of "standing" in Black Jack, where the player declares they will draw no more cards.

    player: Player that is standing
    '''

    return

def count_hand(player):
    '''
    Function that counts the point value in the given players hand.

    player: Player whose points are being calculated.
    '''

    point = 0
    for card in player.hand:
        point = point + card.point

    return point

def check_black_jack(player):
    '''
    Function to check if the player's starting hand is 21 points, or "Black Jack", which is an auto-win.

    player: Player whose point value is being checked.
    '''

    black_jack = False

    if count_hand(player) == 21:
        black_jack = True

    return black_jack

def check_bust(player):
    '''
    Function to check if the player's hand value has gone above 21 points, which is an automatic loss.

    player: Player whose point value is being checked.
    '''

    bust = False

    if count_hand(player) > 21:
        bust = True

    return bust

def game_setup(players, deck):
    '''
    Creates the starting hands for all the players.

    players: list of players

    deck: deck being used
    '''
    for i in range(2):
        for player in players:
            hidden = False

#            if i == 1:
#                if player.dealer:
#                    hidden = True

            hit(player, deck, hidden=hidden)

    return

def game_status(players, player_titles):
    '''
    Function that prints out the current status of the game.
    '''

    for i, player in enumerate(players):
        print(f'\n{player_titles[i]}:\n{player}\nTheir current hand is worth {count_hand(player)}')
    
        if check_black_jack(player):
            print(f'\n{player_titles[i]} has Black Jack.')

        if check_bust(player):
            print(f'\n{player_titles[i]} has busted.')

def player_turn(player_title):
    '''
    Function to play through a players turn.
    '''

    print(f"\n{player_title}'s turn, would you like to hit or stand?")
    print("\n1. Hit\n2. Stand")

    valid_input = False

    while valid_input == False:
        player_choice = int(input(f'\nChoice: '))

        if player_choice in [1,2]:
            valid_input = True
        else:
            player_choice = int(input(f'\nInvalid Input, try again'))

    return player_choice


