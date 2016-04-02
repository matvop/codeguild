# word count program created 3.24
# Find a book on Project Gutenberg. Download it as a UTF-8 text file.
#
# Count how often each unique word is used, then print the most frequent
#  top 10 out with their counts.
# Count how often each unique pair of words is used, then print the most
#  frequent top 10 out with their counts.

# import urllib.request
# def parse_txt_into_list_of_lines():
#     """Parses the main Oregon usgs rain station index webpage into a list of lines"""
#     with urllib.request.urlopen('http://www.gutenberg.org/cache/epub/1342/pg1342.txt') as data_file:
#         book_line_data = [byte_line.decode('utf-8') for byte_line in data_file]
#     return book_line_data

# def parse_txt_into_list_of_lines():
#     with open('C:\Users\Matt\codeguild\extras\p_and_p.txt') as p_and_p:
#         book_line_data = p_and_p.readlines() #creates a list of lines
#     return book_line_data
def parse_txt_into_list_of_lines():
    with open('C:\\Users\\Fizix\\Desktop\\pg1342.txt') as p_and_p:
        book_line_data = p_and_p.readlines()
    return book_line_data

def normalize_word(word):
    word = word.strip('.,:;"()$-!?<>[]_').lower()
    return word

def normalize_words():
    all_cleaned_words = [normalize_word(word) for word in split_lines_into_words(book_line_data)]
    return all_cleaned_words

def count_word_occurrences():
    """Counts the occurrences of each word in the normalized_word_list and
    creates the dict words_and_counts that contains each word and the # of
    times it occurs"""    #use a collections.Counter instead
    words_and_counts = {}
    for word in normalize_words(): #analyses the values
        if word not in words_and_counts:
            words_and_counts[word] = 1 #adds 1 to the count if the word is not found
        else:
            words_and_counts[word] += 1 #increases the count by 1 if word already exists
    return words_and_counts

def split_lines_into_words(book_line_data):
    all_words = []
    for line in book_line_data: #analyses the values in the list book_line_data
        all_words += line.split() #splits the string apart and adds each value(word) split to all_words
    return all_words

book_line_data = parse_txt_into_list_of_lines()
all_words = split_lines_into_words(book_line_data)
words_and_counts = count_word_occurrences()
sorted_by_occurrence = sorted(words_and_counts.keys(), key=words_and_counts.get, reverse=True)
print(sorted_by_occurrence[:10])
