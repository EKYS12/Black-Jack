from deck import Deck
from player import Player

def hit(player, deck, hidden=False):
    card = deck.draw()

    if hidden:
        # hide_card(card)
        return

    player.hand.append(card)

    return

def stand(player):

    return

def count_hand(player):

    point = 0
    for card in player.hand():
        point = point + card.point()

    return points

def check_black_jack(player):

    black_jack = False

    if count_hand(player) == 21:
        black_jack = True

    return black_jack

def check_bust(player):

    bust = False

    if count_hand(player) > 21:
        bust = True

    return bust

def game_setup(dealer, players, deck):
    for i in range(2):
        for player in players:
            hidden = False

            if i == 1:
                if player.dealer:
                    hidden = True

            hit(player, deck, hidden=hidden)

    return

# Start of Game

dealer = Player(dealer=True)

player1 = Player()

player2 = Player()

players = [player1, player2, dealer]

deck = Deck()

deck.shuffle()

game_setup(dealer, players, deck)

for player in players:
    print(player.hand)
