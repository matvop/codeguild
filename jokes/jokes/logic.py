import os
import json


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
