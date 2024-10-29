'''
This is the Player class that will be used to represent players in the game. Players will have a hand that contains the cards that the player owns. The class contains a dealer flag that determines if they are the dealer or not.
'''

class Player:
    def __init__(self, dealer=False):

        self.hand = []
        self.dealer = dealer
        self.bust = False

    def __str__(self):
        '''
        String print out representation of the player and their hand.
        '''

        player_str = "This Player's current hand is:"

        for card in self.hand:
            player_str = player_str + f'\n{str(card)}'

        return player_str
