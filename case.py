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


def convert_snake(orig_string):
    print('CamelCase: ' + ''.join([i[0].upper() + i[1:] for i in orig_string.split('_')]))  # CamelCase
    print('kebab-case: ' + '-'.join([i for i in orig_string.split('_')]))  # kebab-case
    print('CONSTANT_CASE: ' + '_'.join([i for i in orig_string.split('_')]).upper())  # CONSTANT_CASE


def convert_camel(orig_string):
    print('snake_case: ' + '_'.join([i for i in re.findall('[A-Z][^A-Z]*', orig_string)]).lower())  # snake_case
    print('kebab-case: ' + '-'.join([i for i in re.findall('[A-Z][^A-Z]*', orig_string)]).lower())  # kebab-case
    print('CONSTANT_CASE: ' + '_'.join([i for i in re.findall('[A-Z][^A-Z]*', orig_string)]).upper())  # CONSTANT_CASE


def convert_kebab(orig_string):
    print('CamelCase: ' + ''.join([i[0].upper() + i[1:] for i in orig_string.split('-')]))  # CamelCase
    print('snake_case: ' + '_'.join([i for i in orig_string.split('-')]))  # snake_case
    print('CONSTANT_CASE: ' + '_'.join([i for i in orig_string.split('-')]).upper())  # CONSTANT_CASE


def convert_constant(orig_string):
    print('CamelCase: ' + ''.join([i[0].upper() + i[1:] for i in orig_string.lower().split('_')]))  # CamelCase
    print('kebab-case: ' + '-'.join([i for i in orig_string.lower().split('_')]))  # kebab
    print('snake_case: ' + orig_string.lower())  # snake


def prompt_for_string():
    return input('Please enter a string to be converted\n> ')


def main():
    orig_string = prompt_for_string()
    if orig_string == orig_string.upper():
        return convert_constant(orig_string)
    if '-' in orig_string:
        return convert_kebab(orig_string)
    if orig_string in re.split('_|-|;|, ', orig_string):
        return convert_camel(orig_string)
    if orig_string == orig_string.lower():
        return convert_snake(orig_string)


main()
