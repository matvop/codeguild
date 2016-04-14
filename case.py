# Practice: Case Conversion
# Write a program that prompts the user for a word in `snake_case`,
# then converts and prints it out in `CamelCase`.
# Also do the reverse conversion.
#
# Advanced
# * Write functions to handle `kebab-case` and `CONSTANT_CASE`.
# * Write functions to auto-detect which case is input.
# * Automatically print out all other cases on input.
# * Come up with a original-case-agnostic intermediate representation.
import re


def snake_to_camel():
    print('Your word: ' + prompt_for_string())
    new_list = prompt_for_string().split('_')
    camel_case = ''.join([i[0].upper() + i[1:] for i in new_list])
    return camel_case


def convert_to_camel():
    print('Your word: ' + prompt_for_string())
    string_list = re.split('_|-|;|,|\*', prompt_for_string())
    print(string_list)
    camel_case = ''.join([i[0].upper() + i[1:] for i in string_list])
    return camel_case


def camel_to_snake():
    print('Your string: ' + prompt_for_string())
    string_list = re.findall('[A-Z][^A-Z]*', prompt_for_string())
    snake_case = '_'.join([i for i in string_list])
    return snake_case.lower()


# def convert_snake():
# def convert_camel():
# def convert_kebab():
# def convert_constant():


def detect_orig_case():
    list_of_func = ['snake_case', 'CamelCase', 'kebab-case', 'CONSTANT_CASE']
    orig_string = prompt_for_string()
    if orig_string == orig_string.upper():
        print(list_of_func[3])
        convert_constant()
    if '-' in orig_string:
        print(list_of_func[2])
        convert_kebab()
        return orig_string
    if orig_string in re.split('_|-|;|, ', orig_string):
        print(list_of_func[1])
        convert_camel()
    if orig_string.split('_') != re.split('-|;|,| ', orig_string):
        print(list_of_func[0])
        convert_snake()
    else:
        print('Not Found')

def prompt_for_string():
    return input('Please enter a string to be converted\n> ')

detect_orig_case()
