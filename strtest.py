import random


with open('google-10000-english-usa.txt') as dictionary:
    all_words = dictionary.readlines()

selected_word = ''
while len(selected_word) < 4:
    selected_word = random.choice(all_words).strip()

print(selected_word)
