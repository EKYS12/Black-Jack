from util.deck import Deck
from util.player import Player

def hit(player, deck):
    card = deck.draw()

    if player.dealer():
        # hide_card(card)

    player.hand.append(card)

    return

def stand(player):

    return

def check_bust(player):

    return
