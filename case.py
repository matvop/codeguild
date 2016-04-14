# Practice: Case Conversion
# Write a program that prompts the user for a word in `snake_case`, then converts and prints it out in `CamelCase`.
# Also do the reverse conversion.
#
# Advanced
# * Write functions to handle `kebab-case` and `CONSTANT_CASE`.
# * Write functions to auto-detect which case is input.
# * Automatically print out all other cases on input.
# * Come up with a original-case-agnostic intermediate representation.
import re


def snake_to_camel(orig_string):
    orig_string = input('Please enter word/string in snake_case: ').lower()
    print('Your word: ' + orig_string)
    new_list = orig_string.split('_')
    camel_case = ''.join([i[0].upper() + i[1:] for i in new_list])
    return camel_case


def convert_to_camel(orig_string):
    orig_string = input('Please enter word/string: ').lower()
    print('Your word: ' + orig_string)
    string_list = re.split('_|-|;|,|\*', orig_string)
    print(string_list)
    camel_case = ''.join([i[0].upper() + i[1:] for i in string_list])
    return camel_case


def camel_to_snake(orig_string):
    camel_string = input('Please enter a CamelCase string to be converted '
        'to snake_case\n> ')
    print('Your string: ' + orig_string)
    string_list = re.findall('[A-Z][^A-Z]*', orig_string)
    snake_case = '_'.join([i for i in string_list])
    return snake_case.lower()


def prompt_for_input():
    orig_string = input('Please enter a string to be converted\n> ')
camel_to_snake()
