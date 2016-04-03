# word count program created 3.24
# Find a book on Project Gutenberg. Download it as a UTF-8 text file.
#
# Count how often each unique word is used, then print the most frequent
#  top 10 out with their counts.
# Count how often each unique pair of words is used, then print the most
#  frequent top 10 out with their counts.

#inactive functions here for now
# import urllib.request
# def parse_txt_into_list_of_lines():
# with urllib.request.urlopen(
#     'http://www.gutenberg.org/cache/epub/1342/pg1342.txt') as data_file:
#     book_line_data = [byte_line.decode(
#         'utf-8') for byte_line in data_file]
# return book_line_data
# def parse_txt_into_list_of_lines():
#     with open('C:\Users\Matt\codeguild\extras\p_and_p.txt') as p_and_p:
#         book_line_data = p_and_p.readlines() #creates a list of lines
#     return book_line_data

from collections import Counter

def parse_txt_into_list_of_lines():
    with open('C:\\Users\\Fizix\\Desktop\\pg1342.txt') as p_and_p:
        book_line_data = p_and_p.readlines()
    return book_line_data

def split_lines_into_words():
    all_words = []
    for line in parse_txt_into_list_of_lines():
        all_words += line.split()
    return all_words

def normalize_word(word):
    word = word.strip('.,:;"()$-!?<>[]_').lower()
    return word

def normalize_words():
    all_cleaned_words = [
        normalize_word(word) for word in split_lines_into_words()
    ]
    return all_cleaned_words

def count_word_occurrences():
    words_and_counts = Counter(normalize_words())
    return words_and_counts

def print_top_10(n = 10):
    print('\n{:<5} {:<5}'.format('Word:', 'Count:\n'))
    for word, count in count_word_occurrences().most_common(n):
        print('{:<5} {:<5}'.format(word, count))

print_top_10()
