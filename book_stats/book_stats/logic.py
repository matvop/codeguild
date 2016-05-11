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

def get_book_title():
    global book_location
    dir_list = book_location.split('\\')
    title_and_ext = dir_list[-1].split('.')
    title = title_and_ext[0]
    return title

def print_top_10(n=10):
    global dictionary
    top10_list = []
    for word, count in dictionary.most_common(n):
        top10_list += ('{}: {} '.format(word.title(), count))
    return top10_list

def parse_txt_into_list_of_lines(book_location):
    with open(book_location) as book_file:
        book_line_data = book_file.readlines()
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
    global book_location
    book_line_data = parse_txt_into_list_of_lines(book_location)
    words_and_strings = split_lines_into_words(book_line_data)
    cleaned_word_list = normalize_words(words_and_strings)
    words_and_counts = count_word_occurrences(cleaned_word_list)
    return words_and_counts

book_location = 'C:\\Users\\Matt\\codeguild\\extras\\Pride and Prejudice.txt'
dictionary = main()
