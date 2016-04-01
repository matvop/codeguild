import time
from sys import stdout

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
def loaddot():
    stdout.write("."*(dots%5 + 1))
    time.sleep(1)

visited_cities = []

print('Please select which city you would like to visit from the list below.')
print("""
Albany
Boston
New York
Philadelphia
Portland
""")
travel_choice = input('>')

while len(visited_cities) <2:
    if travel_choice == 'Boston':
        dots = 0
        visited_cities += travel_choice
        print('You have selected Boston.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['Boston'])
        travel_choice = input('>')

    if travel_choice == 'Portland':
        dots = 0
        visited_cities += travel_choice
        print('You have chosen to travel to Portland.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['Portland'])
        travel_choice = input('>')

    if travel_choice == 'New York':
        dots = 0
        visited_cities += travel_choice
        print('You have chosen to visit New York.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['New York'])
        travel_choice = input('>')

    if travel_choice == 'Philadelphia':
        dots = 0
        visited_cities += travel_choice
        print('You have chosen Philadelphia.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['Philadelphia'])
        travel_choice = input('>')

    if travel_choice == 'Albany':
        dots = 0
        visited_cities += travel_choice
        print('You have selected Albany.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['Albany'])
        travel_choice = input('>')

while len(visited_cities) >1:
    if travel_choice == 'Boston':
        dots = 0
        visited_cities += travel_choice
        print('You have selected Boston.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print('You can reach the following cities in two hops.')
        two_hop_boston = city_to_accessible_cities['Boston']
        travel_choice = input('>')

    if travel_choice == 'Portland':
        dots = 0
        visited_cities += travel_choice
        print('You have chosen to travel to Portland.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['Portland'])
        travel_choice = input('>')

    if travel_choice == 'New York':
        dots = 0
        visited_cities += travel_choice
        print('You have chosen to visit New York.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['New York'])
        travel_choice = input('>')

    if travel_choice == 'Philadelphia':
        dots = 0
        visited_cities += travel_choice
        print('You have chosen Philadelphia.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['Philadelphia'])
        travel_choice = input('>')

    if travel_choice == 'Albany':
        dots = 0
        visited_cities += travel_choice
        print('You have selected Albany.')
        while(dots < 5):
            stdout.write("Traveling")
            loaddot()
            dots += 1
            stdout.flush()
            print('')
        print('You have arrived. Please choose the next city you would like to visit:')
        print(city_to_accessible_cities['Albany'])
        travel_choice = input('>')
