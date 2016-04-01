#fuel cost trip calculator created 3.16.2016
print('')
print('')
print('This program will attempt to determine the total fuel cost for your road trip.')
print('Please answer the following questions...')

print('')
print('What is the distance you will travel? (in miles)')
distance = int(input())

print('')
print('How many miles per gallon can your vehicle achieve?')
mpg = int(input())

print('')
print('What is the current cost of fuel? (per gallon)')
fuelprice = int(input())

totgal = int()
totgal = (distance/mpg)

tripcost = int()
tripcost = (totgal*fuelprice)

print('')
print('Your total trip will cost: $' + str(tripcost))
print('')
print('')
print('')
