# word count program created 3.24
# Find a book on Project Gutenberg. Download it as a UTF-8 text file.
#
# Count how often each unique word is used, then print the most frequent top 10 out with their counts.
# Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.
all_words = [] #creates an empty list called all_words
words_and_counts={} #creates an empty dict called words_and_counts
word = ''

def parse_txt_into_list_of_lines():
    with open('p_and_p.txt') as p_and_p: #opens and reads p_and_p.txt to memory as var p_and_p
        book_line_data = p_and_p.readlines() #creates a list of values from the lines in p_and_p called book_line_data
    return book_line_data
def normalize_word(word):
    word = word.strip('.,:;"()$-!?<>[]_').lower()
    return word
def normalize_words(all_words):
    all_cleaned_words = []
    for word in all_words:
        cleaned_word = normalize_word(word)
        all_cleaned_words.append(cleaned_word)
    return all_cleaned_words
#List comprehension of normalize_words [normalize_word(word) for word in all_words]
def count_word_occurances(normalized_word_list, words_and_counts):
    """Counts the occurances of each word in the normalized_word_list and creates the dict words_and_counts that contains each word and the # of times it occurs"""
    for word in normalized_word_list: #analyses the values in the normalized_word_list
        if word not in words_and_counts:
            words_and_counts[word] = 1 #adds 1 to the count of word in words_and_counts dict if the word is not found
        else:
            words_and_counts[word] += 1 #increases the count by 1 of word if it already exists
    return words_and_counts
def split_lines_into_words(book_line_data, all_words):
    for line in book_line_data: #analyses the values in the list book_line_data
        all_words += line.split() #splits the string apart using default delimiter(spaces) and adds each value(word) split to all_words
    return all_words

book_line_data = parse_txt_into_list_of_lines()
all_words = split_lines_into_words(book_line_data, all_words)
normalized_word_list = normalize_words(all_words)
words_and_counts = count_word_occurances(normalized_word_list, words_and_counts)
sorted_by_occurance = sorted(words_and_counts.keys(), key=words_and_counts.get, reverse=True)
print(sorted_by_occurance[:10])
print(normalized_word_list)
