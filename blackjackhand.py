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
    suits = ['C', 'D', 'H', 'S']

    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def __repr__(self):
        card_string = 'Card({}{})'.format(self.name, self.suit)
        return card_string

    def generate_rand_card(self):
        card = Card(random.choice(Card.names), random.choice(Card.suits))
        return card

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
       return 'Hand({})'.format(self.cards)

    def add_card(self, card):
        self.cards.append(Card.generate_rand_card(self))
        print('Added {} to your hand'.format(self.cards[-1]))
        # this is where to add option to remove the card if it matches another card_string
        # for card in self.cards:
        #     if card == card:
        #         print('this actually works?!')

    def score(self, player_hand):
        points = 0
        for card in player_hand:
            if card[0] in Card.names[-3:]:
                points += 10
            if card[0] in Card.names[1:10]:
                points += int(card[0])
            if card[0:2] == '10':
                points += int(card[0:2])
            if card[0] == 'A':
                points += 1
        for card in player_hand:
            for s in card:
                if 'A' in s and points + 11 <= 21:
                    points += 10
        return 'You scored {} points!'.format(points)


# card = [random.choice(Card.names), random.choice(Card.suits)]

my_card = [Card(random.choice(Card.names), random.choice(Card.suits))]
print(my_card)
my_hand = Hand(my_card)
print(my_hand)
my_hand.add_card(my_card)
print(my_hand)
my_hand.score(my_hand)
print(my_score)

custom_hand = print(input(str("Please enter a hand to be scored(i.e. 'k q' or 'kd qh'): ")).upper().split())
print(custom_hand)
my_hand = Hand(custom_hand)
print(my_hand)
print(Hand.score(my_hand))
