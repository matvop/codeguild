#Practice: Farkle dice game
import random
import os
os.system('cls')

play = input('Are you ready to roll? [y/n]: ' )
dice_num = 5
#hold = 'n'
#number_of_saved_dice
dice_list = []
score_list = []

while dice_num != 0 and play == 'y':
    rand_num = 4 #random.randint(1,6)
    dice_list.append(rand_num)
    dice_num -= 1
if dice_list.count(1) >= 3:
    score_list.append(1000)
    dice_list.pop(1)
if dice_list.count(2) >= 3:
    score_list.append(200)
    dice_list.pop(2)
if dice_list.count(3) >= 3:
    score_list.append(300)
    dice_list.pop(3)
if dice_list.count(4) >= 3:
    score_list.append(400)
    dice_list.pop(4)
if dice_list.count(5) >= 3:
    score_list.append(500)
    dice_list.pop(5)
if dice_list.count(5) == 2:
    score_list.append(50)
    score_list.append(50)
    dice_list.pop(5)
if dice_list.count(6) >= 3:
    score_list.append(600)
    dice_list.pop(6)
print(dice_list)
print(score_list)
print(sum(score_list))
#if num == 1:
#    print(dice_list.count(1) + ' ones were rolled')
#if num == 5:
    #print(dice_list.count(5) + ' fives were rolled')
    #print('you scored ' + (dice_list.count(num)*50))
