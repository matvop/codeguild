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
    def __init__(self, points):
        # self.suit = suit
        self.points = points

    # def score_the_card(self):
    #     self.points


class Hand:
    def __init__(self, list_of_cards, sum_of_points):
        self.possible_cards_with_score = [
            ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7],
            ['8', 8], ['9', 9], ['10', 10], ['J', 10], ['Q', 10], ['K', 10],
            ['A', 11]]
        self.possible_cards = [i[0][0] for i in self.possible_cards_with_score]
        self.list_of_cards = list_of_cards
        self.sum_of_points = sum_of_points

    def __repr__(self):
        my_str = 'You scored {}!'.format(self.sum_of_points)
        # I have absolutely no idea what this does

    def add_card_to_hand(self):
        self.list_of_cards.append(random.choice(self.possible_cards))
        return self.list_of_cards

    def score_the_hand(self, list_of_cards):
        # print([i[1] for i in self.possible_cards_with_score])
        self.sum_of_points = sum([i[1] for i in self.possible_cards_with_score
                                  if i[0] in self.list_of_cards])
        print(self.sum_of_points)


myhand = Hand([], 0)
list_of_cards = myhand.add_card_to_hand()
run = True
while run:
    list_of_cards = myhand.add_card_to_hand()
    print(list_of_cards)
    yayornay = input('Draw another card? [y/n]: ')
    if yayornay == 'y':
        run = True
    else:
        print('You scored {}!'.format(myhand.score_the_hand(list_of_cards)))
        run = False
