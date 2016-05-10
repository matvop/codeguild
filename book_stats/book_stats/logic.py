from collections import Counter
import re


def check_count(word):
    global dictionary
    count = dictionary.get(word)
    if count:
        result = '{}: {}'.format(word.title(), count)
    else:
        result = '{}: {}'.format(word.title(), 0)
    return result

def print_top_10(n=10):
    global dictionary
    print('\n{:<5} {:<5}'.format('Word:', 'Count:\n'))
    for word, count in dictionary.most_common(n):
        print('{:<5} {:<5}'.format(word, count))

def parse_txt_into_list_of_lines():
    with open('C:\\Users\\Matt\\codeguild\\extras\\p_and_p.txt') as p_and_p:
        book_line_data = p_and_p.readlines()
    return book_line_data

def split_lines_into_words(book_line_data):
    all_words = []
    for line in book_line_data:
        all_words += re.findall(r"[\w']+", line)
    return all_words

def normalize_word(word):
    word = word.strip('.,:;"()$-!?<>[]_').lower()
    return word

def normalize_words(words_and_strings):
    all_cleaned_words = [normalize_word(word) for
                         word in words_and_strings]
    return all_cleaned_words

def count_word_occurrences(cleaned_word_list):
    words_and_counts = Counter(cleaned_word_list)
    return words_and_counts


def main():
    book_line_data = parse_txt_into_list_of_lines()
    words_and_strings = split_lines_into_words(book_line_data)
    cleaned_word_list = normalize_words(words_and_strings)
    words_and_counts = count_word_occurrences(cleaned_word_list)
    return words_and_counts


dictionary = main()
