#madlib program created 3.16.2016
def get_adj():
    """Prompt user for first adjective"""
    return input('\nPlease enter an adjective: ')
def get_noun():
    """Prompt user to enter a noun."""
    return input('\nPlease enter a noun: ')
def get_food():
    """Prompt user for food choice"""
    return input('\nPlease choose a type of food: ')
def get_name():
    """Prompt user for the name of someone in the room."""
    return input('\nPlease enter the name of someone in the room: ')
def get_adj2():
    """Prompt user for a second adjective."""
    return input('\nPlease enter another adjective: ')
def get_noun2():
    """Prompt user for another noun."""
    return input('\nPlease select one more noun: ')
def get_city():
    """Prompt user for the name of a city."""
    return input('\nPlease enter the name of a city: ')
def get_condiment():
    """Prompt user for a condiment."""
    return input('\nPlease enter your favorite condiment: ')
def build_madlib():
    """Build the madlib from the user's input."""
    print('\nThere are many ' + get_adj() + ' ways to choose a ' + get_noun() +
    " to eat. You could ask for recommendations from your friends and family. Just don't ask Uncle "
    + get_name() + '-he only eats ' + get_adj2() + ' ' + get_food() + ' with '
    + get_condiment() + ' and fish oil sauce. If your friends and family are no help, try checking out the '
    + get_noun2() + ' Review in The ' + get_city() + ' Times.\n\n')

build_madlib()
