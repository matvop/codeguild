#madlib program created by Matt Voelpel 3.16.2016
def get_adj():
    """Prompt user for first adjective"""
    return input('Please enter an adjective: ')
def get_noun():
    """Prompt user to enter a noun."""
    return input('Please enter a noun: ')
def get_food():
    """Prompt user for food choice"""
    return input('Please choose a type of food: ')
def get_name():
    """Prompt user for the name of someone in the room."""
    return input('Please enter the name of someone in the room: ')
def get_adj2():
    """Prompt user for a second adjective."""
    return input('Please enter another adjective: ')
def get_noun2():
    """Prompt user for another noun."""
    return input('Please select one more noun: ')
def get_city():
    """Prompt user for the name of a city."""
    return input('Please enter the name of a city: ')
def get_condiment():
    """Prompt user for a condiment."""
    return input('Please enter your favorite condiment: ')
def build_madlib(adj, noun, name, adj2, food, condiment, noun2, city):
    """Build the madlib from the user's input."""
    return 'There are many ' + adj + ' ways to choose a ' + noun + " to eat. You could ask for recommendations from your friends and family. Just don't ask Uncle " + name + '-he only eats ' + adj2 + ' ' + food + ' with ' + condiment + ' and fish oil sauce. If your friends and family are no help, try checking out the ' + noun2 + ' Review in The ' + city + ' Times.'
print('')
print('')

adj = get_adj()
noun = get_noun()
name = get_name()
adj2 = get_adj2()
food = get_food()
condiment = get_condiment()
noun2 = get_noun2()
city = get_city()
madlib = build_madlib(adj, noun, name, adj2, food, condiment, noun2, city)

print(madlib)
