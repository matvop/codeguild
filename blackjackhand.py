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
    names = ['A', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'Q', 'K']
    suits = ['c', 'd', 'h', 's']
    rand_names = random.choice(names)
    rand_suits = random.choice(suits)

    def __init__(self, name, suit):
        self.suit = suit
        self.name = name

    def __repr__(self):
        card_string = '{}{}'.format(self.name, self.suit)
        return card_string


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
       hand_string = 'Your Hand: '
       for card in self.cards:
           if self.cards:
               hand_string += '{}'.format(card)
       return 'Hand: {}'.format(self.cards)

    def add_card(self):
        self.cards.append(Card.rand_names + Card.rand_suits)

    def score(self):
        points = 0
        for card in self.cards:
            if card[0] in Card.names[-3:]:
                print('name is: ' + card[0])
                points += 10
            if card[0] in Card.names[1:10]:
                print('name is: ' + card[0])
                points += int(card[0])
            if card[0:2] == '10':
                print('name is: ' + card[0:2])
                points += int(card[0:2])
            if card[0] == 'A':
                print('name is: ' + card[0])
                points += 1
        for card in self.cards:
            if 'A' in self.cards and points + 11 <= 21:
                print('bonus points for ace awarded! ')
                points += 10
        return points
                    # points += int(card[-1])
            # convert string character at -1 into int and add its name to points


my_hand = Hand([random.choice(Card.names) + random.choice(Card.suits)])
print(my_hand)
Hand.add_card(my_hand)
print(my_hand)
print(Hand.score(my_hand))
