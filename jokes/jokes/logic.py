import os
import json
from random import randint


def gen_random_index():
    rand_num = randint(0,5)
    return rand_num

def get_random_color():
    color_list = ['blue', 'red', 'green', 'purple', 'orange', 'cyan']
    rand_color = color_list[gen_random_index()]
    return rand_color

def get_colors():
    color_list = ['blue', 'red', 'green', 'purple', 'orange', 'cyan']
    return color_list

def load_joke_database():
    with open(os.path.join(__location__, 'jokes_database.txt')) as data_file:
        database = eval(data_file.read())
        return database

def save_joke(joke):
    """Save a new joke"""
    global jokes
    jokes.append(joke)
    save_jokes_database(jokes)

def get_all_jokes():
    """Returns all saved jokes as a list of strings"""
    return jokes

def save_jokes_database(jokes):
    with open(os.path.join(__location__, 'jokes_database.txt'), 'w') as data_file:
        json.dump(jokes, data_file)


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

jokes = load_joke_database()
