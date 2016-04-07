# Practice: Blackjack Hand
# Implement scoring a single hand of blackjack.
#
# Cards have point values. Aces are 1 or 11, number cards are their number,
# face cards are all 10. A hand is worth the sum of all the points of the cards
# in it.
# An ace is worth 1 when the hand it's a part of would be over 21 if it was
# worth 11.
#
# Make a class that represents a card.
# Make a class that represents a hand.
# Add functions that adds a card to a hand, one that scores a hand, and one
# that returns if the score is over 21.
# Allow a user to type in a hand and have it be converted into card objects
# and then scored.
import random


class Card:
    names = ['2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['c', 'd', 'h', 's']

    def __init__(self, names, suits):
        self.suits = suits
        self.names = names

    def __repr__(self):
        response = self.names + self.suits
        return response

class Hand:
    def __init__(self, cards):
        self.cards = []

    def __repr__(self):
        if self.cards:
           response = ''
           for card in self.cards:
               response += str(card) + ' '
           else:
               reponse = '<empty>'
           return response

    def add_card(self, card):
        self.cards.append(card)

    def score(self, points):
        if names[0:10] in self.cards:
            points += 10
        # if self.names in :
        # points =

my_hand = Hand()
print(my_hand)
