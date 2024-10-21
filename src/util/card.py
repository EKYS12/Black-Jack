'''
This file contains the Card class that will be used in the game. Cards should only exist in a deck, or a player's hand.
'''

class Card:
    def __init__(self, value, suit, face=False, ace=False):
        '''
        Initialize with a string numerical or letter for the value of the vard and a string for the suit of the card.Include a boolean for whether the card is a face card or an ace.
        '''

        self.value = value
        self.suit = suit

        # Set an integer value for the point value of a card.
        if self.value in ['J', 'Q', 'K']:
            self.face = True
            self.point = 10 
        elif self.value == 'A':
            self.ace = True
            self.point = 11  
        else:
            self.point = int(self.value)

    def __str__(self):
        # String representation of object
        card_str = f'{self.value} of {self.suit}'
        return card_str

