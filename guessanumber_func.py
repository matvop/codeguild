#guessanumber_func created by Matt Voelpel 3.21.2016
#v2 modified to include functions and remove play again

import random
def guess(max_guesses, guesses_taken):
    """Prompts the user to guess a number. Reurnted as chosen_num"""
    if guesses_taken == 0:
        print('Guess a number between 1 and 100. You have only ' + str(max_guesses) + ' guesses, so choose wisely.')
    if guesses_taken > 0 and guesses_taken < max_guesses:
        print('Guess again!')
    chosen_num = int(input())
    return chosen_num

def check_guess(guesses_taken, rand_num, last_guess, chosen_num, max_guesses):
    """Checks the user's guess to the random number generated by the program"""
    if rand_num < chosen_num:
        print('Too high.')
    if rand_num > chosen_num:
        print('Too low.')
    if rand_num != chosen_num and guesses_taken == last_guess:
        print('The maximum number of guesses has been reached.')
    return True

def end_the_game(guesses_taken, max_guesses, should_loop, rand_num, chosen_num):
    if rand_num == chosen_num:
        print('You guessed correctly!')
        #should_loop = False
    if rand_num != chosen_num:
        print('The number I was thinking of was ' + str(rand_num) + '.')
        #should_loop = False
    return False

guesses_taken = 0
max_guesses = 4
last_guess = (max_guesses - 1)
rand_num = random.randint(1,100)
should_loop = True

while should_loop:
    chosen_num = guess(max_guesses, guesses_taken)
    should_loop = check_guess(guesses_taken, rand_num, last_guess, chosen_num, max_guesses)
    guesses_taken += 1
    while guesses_taken == max_guesses and should_loop:
        should_loop = end_the_game(guesses_taken, max_guesses, should_loop, rand_num, chosen_num)
