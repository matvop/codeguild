#Pig Latin Translator
#Enter Sentence
#convert each word to Pig Latin
#Print out translation
#Advanced features: handle vowels(added), punctuation, and capitalization


import os
os.system('cls')        #added to clear screen

run = 'y'

while run.lower() == 'y':
    os.system('cls')
    print('Please enter a sentence to be translated into Pig Latin:')
    print('')
    english_sentence = input()
    sentence_split = english_sentence.split()
    new_sentence = []
    
    for word in sentence_split:
        if word[0] in 'aeiou':
            new_sentence.append(word + 'way')
        #elif word[-1] in '!.?':
            #new_sentence.append(word[1:] + 'ay' + word[-1])
        else:
            new_sentence.append(word[1:] + word[0] + 'ay')

    print(' '.join(new_sentence))
    print('')
    run = input('Would you like to convert another sentence? [y/n]?: ')
print('')
