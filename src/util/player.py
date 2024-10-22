'''
This is the Player class that will be used to represent players in the game. Players will have a hand that contains the cards that the player owns. The class contains a dealer flag that determines if they are the dealer or not.
'''

class Player:
    def __init__(self, dealer=False):

        self.hand = []
        self.dealer = dealer

    def __str__(self):
        '''
        String print out representation of the players hand.
        '''

        hand_str = ""

        for card in self.hand:
            hand_str = hand_str + f'\n{str(card)}'

        return hand_str
