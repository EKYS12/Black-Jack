'''
This file is for the Deck class that will be used in a game of Black Jack. It is where all cards are first generated and drawn from.
'''

import numpy as np
from card import Card

class Deck:
    def __init__(self):
        # Values of Cards
        self.values = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

        # Suit of Cards
        self.suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

        self.stack = []

        for suit in self.suits:
            for value in self.values:
                self.stack.append(Card(value, suit))

    def __str__(self):
        '''
        String print out representation of the deck of cards.
        '''

        deck_str = ""

        for card in self.stack:
            deck_str = deck_str + f'\n{str(card)}'

        return deck_str

    def shuffle(self, seed=0000):
        '''
        Method that scrambles deck

        seed: Default=1000. Seed number for reproducable shuffles.
        '''

        np.random.seed(seed)

        print(f'\n\nRandomSeed: {seed}')

        np.random.shuffle(self.stack)

    def draw(self):
        '''
        Method that draws a card from the deck by removing the top card of the deck while returning the card that is being removed.
        '''
        if self.stack:
            return self.stack.pop(0)
        else:
            raise ValueError('Deck is empty')

