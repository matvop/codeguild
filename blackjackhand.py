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


class Card(object):
    def __init__(self, names, suits):
        self.names = ['A', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['C', 'D', 'H', 'S']

    def __repr__(self):
        reply = '{}{}'.format(self.names, self.suits)
        return reply

    def generate_card(self):
        card = Card(random.choice(self.names), random.choice(self.suits))
        return card


class Hand(object):
    def __init__(self):
        hand_of_cards = self.hand_of_cards

    hand_of_cards = []

    def __repr__(self):
        return 'Hand({})'.format(self.hand_of_cards)


    def add_card(self):
        self.hand_of_cards.append(Card.generate_card(self))
        print('Added {} to your hand'.format(self.hand_of_cards[-1]))
        # this is where to add option to remove the card if it matches another
        # card_string
        # for card in self.hand_of_cards:
        #     if card == card:
        #         print('this actually works?!')

    def score(self, split_hand, the_cards):
        points = 0
        for each in split_hand:
            if each[0] not in the_cards.card_names[0:13]:
                print("Not sure what {0} is, disregarding.".format(each))
            elif each[0] in the_cards.card_names[10:13]:
                points += 10
            elif each[0] in the_cards.card_names[1:10]:
                points += int(each[0])
            elif each[0] == the_cards.card_names[0]:
                if points + 11 > 21:
                    points += 1
                elif points + 11 <= 21:
                    points += 10
        return points

    # def score(self):
    #     points = 0
    #     for card in self.hand_of_cards:
    #         for s in str(card):
    #             if s in Card.names[-3:]:
    #                 points += 10
    #             if s in Card.names[1:10]:
    #                 points += int(s[0])
    #             if '10' == s:
    #                 points += int(s[0:2])
    #             if 'A' == s:
    #                 points += 1
    #     for card in self.hand_of_cards:
    #         for s in str(card):
    #             if 'A' in s and points + 11 <= 21:
    #                 points += 10
    #     return 'You scored {} points!'.format(points)


my_card = Card()
print(my_card)
my_hand = Hand()
print(my_hand)
my_card.generate_card()
# print(my_hand)
# print(my_hand.score())
# custom_hand = print(input(str("Please enter a hand to be scored(i.e. 'k q' or 'kd qh'): ")).upper().split())
# print(custom_hand)
# my_card = (custom_hand[0])
# print(my_card)
# my_hand = Hand(custom_hand)
# print(my_hand.score())
