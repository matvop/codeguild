#Hangman game created by Matt Voelpel on 3.22.2016
import random
import os
correct_letters = []
missed_letters = []
mistakes_made = 0
mug_of_beer = '''
             _, . '__ .
          '_(_0o),(__)o().
        ,o(__),_)o(_)O,(__)o
      o(_,-o(_ )(),(__(_)oO)_
      .O(__)o,__).(_ )o(_)Oo_)
  .----|   |   |   |   |   |_)0
 /  .--|   |   |   |   |   |,_)
|  /   |   |   |   |   |   |o(_)
|  |   |   |   |   |   |   |_/`)
|  |   |   |   |   |   |   |O_)
|  |   |   |   |   |   |   |
|  |   |   |   |   |   |   |
|  |   |   |   |   |   |   |
|  \   |   |   |   |   |   |
 \  '--|   |   |   |   |   |
  '----|   |   |   |   |   |
       |   |   |   |   |   |
       |   |   |   |   |   |
       |   |   |   |   |   |
       \   \   \   /   /   /
        `"""""""""""""""""`
'''
hang_a_man = ("""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   |
|   |
|  |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   |
|   |
|  | |
|  | |
|
--------
""")

def random_word_list():
    """Selects a word at random from words and returns as random_word"""
    words = ['CODING', 'SOFTWARE', 'PYTHON', 'JAVASCRIPT', 'ENGINEER', 'DEVELOPER', 'PROGRAMMING', 'FUNCTIONS', 'DJANGO', 'RUBY', 'LITERALS', 'ITERABLES', 'OPERATORS', 'BOOLEAN', 'INTEGER', 'STRING', 'FLOAT', 'LOOP']
    #random_word = words[random.randint(0,len(words)-1)]# - my original method of selecting a random word
    random_word = random.choice(words) #more efficient method of selecing a random word
    return random_word

def blanks_and_correct_letters(secret_word, correct_letters):
    """Coverts letters in the secret_word to underscores(blanks) and replaces blanks with correct_letters when chosen"""
    blanks_and_letters = ''
    for letter in secret_word:
        if letter in correct_letters:
            blanks_and_letters += letter + ' '
        else:
            blanks_and_letters += '_ '
    print(blanks_and_letters)
    print('')

def guess_a_letter(secret_word, correct_letters, missed_letters):
    """Prompts them to guess a letter. Mistakes are tallied for incorrect guesses"""
    print('')
    letter_guess = input('Please choose a letter: ').upper()
    print('')
    if letter_guess in secret_word:
        correct_letters.append(letter_guess)
    else:
        missed_letters.append(letter_guess)
        global mistakes_made
        mistakes_made += 1

def correct_word(secret_word, correct_letters):
    """Converts the correctly guessed letters back into a word."""
    blanks_and_letters = ''
    for letter in secret_word:
        if letter in correct_letters:
            blanks_and_letters += letter + ' '
        else:
            blanks_and_letters += '_ '
    return blanks_and_letters.replace(' ','').replace('_','')

# def play_again(play):
#     play = input('Would you like to play again? [y/n]: ')
#     return play

secret_word = random_word_list() #chooses the secret word from the random word list
print('')
while mistakes_made < (len(hang_a_man)): #game loop
    os.system('cls')
    print("Let's play Hangman!")
    print(hang_a_man[mistakes_made])
    if secret_word == correct_word(secret_word, correct_letters):
        print('Congratulations, you guessed ' + secret_word + ' correctly! Here, have a beer!')
        print(mug_of_beer)
        break
    blanks_and_correct_letters(secret_word, correct_letters)
    print(', '.join(missed_letters))
    guess_a_letter(secret_word, correct_letters, missed_letters)
    #could insert a function that prints out a visual depiction of a hangman here
else:
    print('You did not guess the word {}. Better luck next time!'.format(secret_word))
print('')
