#Hangman game created on 3.22.2016
import random
import os
import winsound
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
hang_a_man = (
"""
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
    words = [
        'CODING', 'SOFTWARE', 'PYTHON', 'JAVASCRIPT', 'ENGINEER',
        'DEVELOPER', 'PROGRAMMING', 'FUNCTIONS', 'DJANGO', 'RUBY', 'LITERALS',
        'ITERABLES', 'OPERATORS', 'BOOLEAN', 'INTEGER', 'STRING', 'FLOAT',
        'LOOP', 'DICTIONARY', 'LIST', 'TERMINAL', 'ARGUMENT', 'TUPLE',
        'COMPILE', 'IMUTABLE', 'MODULE', 'NESTED', 'RETURN', 'SHELL',
        'SOURCE', 'PARSE', 'STATEMENT', 'VARIABLE', 'CLASS'
    ]
    # my original method of selecting a random word
    # random_word = words[random.randint(0,len(words)-1)]
    random_word = random.choice(words) #more efficient
    return random_word

def blanks_and_correct_letters(secret_word, correct_letters):
    """Coverts letters in the secret_word to underscores(blanks) and
    replaces blanks with correct_letters when chosen"""
    blanks_and_letters = ''
    for letter in secret_word:
        if letter in correct_letters:
            blanks_and_letters += letter + ' '
        else:
            blanks_and_letters += '_ '
    print(blanks_and_letters)
    print('')

def guess_a_letter(secret_word, correct_letters, missed_letters):
    """Prompts them to guess a letter. Mistakes are tallied for
    incorrect guesses"""
    print('')
    letter_guess = input('Please choose a letter: ').upper()
    print('')
    if letter_guess in secret_word:
        correct_letters.append(letter_guess)
    else:
        missed_letters.append(letter_guess)
        global mistakes_made
        mistakes_made += 1

def guessed_word(secret_word, correct_letters):
    """Converts the correctly guessed letters back into a word."""
    blanks_and_letters = ''
    for letter in secret_word:
        if letter in correct_letters:
            blanks_and_letters += letter + ' '
        else:
            blanks_and_letters += '_ '
    return blanks_and_letters.replace(' ','').replace('_','')

def play_again(play):
    play = input('Would you like to play again? [y/n]: ')
    global mistakes_made
    mistakes_made = 0
    global missed_letters
    missed_letters = []
    global correct_letters
    correct_letters = []
    return play

def tada():
    winsound.PlaySound('C:\\Windows\\Media\\tada.wav', winsound.SND_FILENAME)
# def wa_wa_wa():
    # winsound.PlaySound('C:\\Users\\Matt\\codeguild\\misc\\wa_wa_wa.wav',
    #     winsound.SND_FILENAME)
# def bg_music():
#     winsound.PlaySound('C:\\Users\\Matt\\codeguild\\misc\\hang_em_high.wav',
#         winsound.SND_FILENAME | winsound.SND_ASYNC)

play = 'y'
while play.lower() == 'y':
    # bg_music()
    # have game choose the secret word from the random word list
    secret_word = random_word_list()
    # start the game loop
    while mistakes_made < (len(hang_a_man)):
        os.system('cls')
        # print Let's play hangman!!!
        print("\nLet's play Hangman!")
        # print hangman picture at the same position as the # of mistakes made
        print(hang_a_man[mistakes_made])
        if secret_word == guessed_word(secret_word, correct_letters):
            print(
                'Congratulations, you guessed ' + secret_word +
                    ' correctly! Here, have a beer!'
            )
            print(mug_of_beer)
            tada()
            play = play_again(play)
            break
        blanks_and_correct_letters(secret_word, correct_letters)
        print(', '.join(missed_letters))
        guess_a_letter(secret_word, correct_letters, missed_letters)
    else:
        print(
            'You did not guess the word {}. Better luck next time!\n'
                .format(secret_word)
        )
        # wa_wa_wa()
        play = play_again(play)
