#guessanumber v2 created by Matt Voelpel 3.16.2016
#modified to include an option to play again and allow an easy way to
#adjust the max # of guesses - future updates: prevent error from improper
#keystroke entry

import random
print('')
print('')

play = 'y'

while play.lower() == 'y':

    guesses_taken = 0
    max_guesses = 4
    rand_num = random.randint(1,100)

    while guesses_taken < int(max_guesses):
        if guesses_taken == 0:
            print('Guess a number between 1 and 100. You have only ' + str(max_guesses) + ' guesses, so choose wisely.')
        if guesses_taken > 0:
            print('Guess again!')
        chosen_num = int(input())
        if rand_num < chosen_num and guesses_taken != (max_guesses - 1):
            print('Too high.')
        elif rand_num < chosen_num and guesses_taken == (max_guesses - 1):
            print('Too high. The maximum number of guesses has been reached.')
        elif rand_num > chosen_num and guesses_taken != (max_guesses - 1):
            print('Too low.')
        elif rand_num > chosen_num and guesses_taken == (max_guesses - 1):
            print('Too low. The maximum number of guesses has been reached.')
        elif rand_num == chosen_num:
            guesses_taken = (max_guesses - 1) #used this instead of break
        guesses_taken += 1

    if rand_num == chosen_num:
        print('You guessed correctly!')
    if rand_num != chosen_num:
        print('The number I was thinking of was ' + str(rand_num) + '.')

    play = input("Would you like to play again? (y/n): ")
    print('')
