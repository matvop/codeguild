#Hangman game created by Matt Voelpel on 3.22.2016
import random
correct_letters = []
missed_letters = []
mistakes_made = 0

def random_word_dict():
    word = ['CODING', 'SOFTWARE', 'PYTHON', 'JAVASCRIPT', 'ENGINEER', 'DEVELOPER', 'PROGRAMMING', 'FUNCTIONS', 'DJANGO', 'RUBY', 'LITERALS', 'ITERABLES', 'OPERATORS', 'BOOLEAN', 'INTEGER', 'STRING', 'FLOAT', 'LOOP']
    random_word = word[random.randint(0,17)]
    return random_word

def blanks_and_correct_letters(secret_word, correct_letters):
    """Create a new list based off of word_length or secret_word_as_list and replace values with underscores"""
    blanks_and_letters = ''
    for letter in secret_word:
        if letter in correct_letters:
            blanks_and_letters += letter + ' '
        else:
            blanks_and_letters += '_ '
    print(blanks_and_letters)

def guess_a_letter(secret_word, correct_letters, missed_letters):
    """Shows player blanks and prompts them to guess a letter. Mistakes are tallied for incorrect guesses"""
    letter_guess = input('Please choose a letter: ').upper()
    if letter_guess in secret_word:
        correct_letters.append(letter_guess)
    else:
        missed_letters.append(letter_guess)
        global mistakes_made
        mistakes_made += 1

def correct_word(secret_word, correct_letters):
    """Create a new list based off of word_length or secret_word_as_list and replace values with underscores"""
    blanks_and_letters = ''
    for letter in secret_word:
        if letter in correct_letters:
            blanks_and_letters += letter + ' '
        else:
            blanks_and_letters += '_ '
    return blanks_and_letters.replace(' ','').replace('_','')

print('')
secret_word = random_word_dict()
while mistakes_made < 7:
    if secret_word == correct_word(secret_word, correct_letters):
        print('Congratulations, you guessed ' + secret_word + ' correctly!')
        break
    blanks_and_correct_letters(secret_word, correct_letters)
    print(', '.join(missed_letters))
    guess_a_letter(secret_word, correct_letters, missed_letters)
else:
    print('You did not guess the word {}'.format(secret_word))
print('')
