#guessanumber_func created 3.21.2016
#modified to use functions
print('')
import random #import random module so that the secret number can be generated
import os #import os module so that the screen can be cleared at the start
def guess(max_guesses, guesses_taken):
    """Prompts the user to guess a number. Returned as chosen_num"""
    if guesses_taken == 0:
        print(
            'Guess a number between 1 and 100. You have only '
                + str(max_guesses) + ' guesses, so choose wisely.'
        )
    if guesses_taken > 0 and guesses_taken < max_guesses:
        print('Guess again!')
    chosen_num = int(input())
    return chosen_num

def add_a_guess(guesses_taken):
    """Adds a guess to the total guesses"""
    guesses_taken += 1
    return guesses_taken

def high_or_low(secret_num, chosen_num):
    """Tells the user how their guess compares to the random number generated
    by the program. Adds a guess to guesses_taken and returns value."""
    if secret_num < chosen_num:
        print('Too high.')
    if secret_num > chosen_num:
        print('Too low.')

def right_or_wrong(guesses_taken, max_guesses, secret_num, chosen_num):
    """Checks if the user's guess is wrong or right, and let's them know."""
    if secret_num == chosen_num:
        print('You chose correctly in ' + str(guesses_taken) + ' guesses!')
    if secret_num != chosen_num and guesses_taken == max_guesses:
        print(
            'The maximum number of ' + str(max_guesses) +
                ' guesses has been reached. The number I was thinking of was '
                + str(secret_num) + '.'
        )

def is_correct(secret_num, chosen_num):
    """Checks if the player's chosen number matches the random number"""
    if secret_num == chosen_num:
        correct_guess = True
    if secret_num != chosen_num:
        correct_guess = False
    return correct_guess

def play_again():
    """Asks user if they would like to play again"""
    play = input('Would you like to play again? [y/n]: ')
    return play

play = 'y'
while play.lower() == 'y':
    os.system('cls')
    guesses_taken = 0
    max_guesses = 6
    secret_num = random.randint(1,100)
    correct_guess = False
    while guesses_taken < int(max_guesses) and correct_guess != True:
        chosen_num = guess(max_guesses, guesses_taken)
        guesses_taken = add_a_guess(guesses_taken)
        high_or_low(secret_num, chosen_num)
        right_or_wrong(guesses_taken, max_guesses, secret_num, chosen_num)
        correct_guess = is_correct(secret_num, chosen_num)
    play = play_again()
print('')
