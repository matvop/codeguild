#dice roller program created by Matt Voelpel 3.16.2016
print('')
print('')
import random
print('How many dice would you like to roll?')

number_of_dice = int(input())
roll_num = 0 #roll number
total = 0 #sum of all die values

while number_of_dice != 0:
    rand_num = random.randint(1,6)
    roll_num += 1
    print('Roll # ' + str(roll_num) + ' came out with ' +str(rand_num))
    number_of_dice -= 1
    total += rand_num

avg = (total/roll_num) #finding the average die value

print('The average roll was ' + str(avg) + '.')
print('')
print('')
