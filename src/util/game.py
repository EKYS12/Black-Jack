'''
This file contains the game logic for Black Jack.
'''

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
    for card in player.hand():
        point = point + card.point()

    return points

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

            if i == 1:
                if player.dealer:
                    hidden = True

            hit(player, deck, hidden=hidden)

    return

# Start of Game

# Create Dealer
dealer = Player(dealer=True)

# Create Players
player1 = Player()

player2 = Player()

# Group players and dealer in a list
players = [player1, player2, dealer]

# Create Deck and shuffle
deck = Deck()

deck.shuffle()

# Set up the game
game_setup(players, deck)

for player in players:
    print(player.hand)
