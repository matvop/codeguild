#guessanumber v1.1 created by Matt Voelpel 3.16.2016
#updated to include
import random
print('')
print('')

guesses_taken = 0
rand_num = random.randint(1,100)

while guesses_taken < 4:
    if guesses_taken == 0:
        print('Guess a number between 1 and 100')
    if guesses_taken > 0:
        print('Guess again!')
    chosen_num = int(input())
    if rand_num < chosen_num and guesses_taken != 3:
        print('Too high.')
    elif rand_num < chosen_num and guesses_taken == 3:
        print('Too high. Maximum number of guess has been reached.')
    elif rand_num > chosen_num and guesses_taken !=3:
        print('Too low.')
    elif rand_num > chosen_num and guesses_taken == 3:
        print('Too low. Maximum number of guess has been reached.')
    elif rand_num == chosen_num:
        guesses_taken = 3 #used this instead of break
    guesses_taken += 1

if rand_num == chosen_num:
    print('You guessed correctly!')
if rand_num != chosen_num:
    print('The number I was thinking of was ' + str(rand_num))
