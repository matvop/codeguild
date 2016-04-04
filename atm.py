# Practice: ATM
# Write a program that functions as a simple ATM for a single account.
#
# An account will be a class: it will have a field for the balance.
#
# Write functions for the account class that:
#
# Deposit to the account.
# Check if enough funds for a withdrawal.
# Withdraw an allowed amount.
# Calculate 0.5% interest on the account.
# Implement a user interface that lets a user pick each of those actions and
# updates the account. After each action it will print the balance.
#
# Advanced
#
# Save the account balance to a file after each operation.
# Read that balance on startup so the balance persists across program starts.
# Add to each account class an account ID number.
# Allow the user to open more than one account.
# Let them perform all of the above operations by account number.
import os
class User:
    def setup(self, account_num, name, balance, pin):
        """Return a User object whose name is *name* and starting
        balance is *balance*."""
        self.account_num = account_num
        self.name = name
        self.balance = database
        self.pin = database

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        print('Your current balance is: {}'.format(self.balance))
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        print('Your current balance is: {}'.format(self.balance))
        return self.balance
        # else:
        #     # enter name and have system generate a new account# based on
        #     # a-z100-999  with blanace 0
        #     print('You have entered an incorrect pin. Goodbye.')
        # else:
        #     # enter name and have system generate a new account# based on
        #     # a-z100-999  with blanace 0
        #     print('create new account here :)')


def open_account_database():
    with open('account_database.txt') as data_file:
        database = eval(data_file.read())
        return database


# database = {'a123':['Matt', 0, '1234'], 'a234':['John', 0,
#     '2345'], 'a345':['Mary', 0, '3456']}

database = open_account_database()
input('Please enter your account number (e.g. a428): ')
print('\nAccount ' + me.account_num + ' has been verified.\n')
me = User()
banking = 'y'
while banking.lower() == 'y':
    os.system('cls')
    # me.setup(
    #     me.account_num,
    #     database[][0],
    #     database[][1],
    #     database[][2])
    print(
        'Welcome {}, would you like to do today?'
            .format(me.name)
    )
    action = int(input("""
    1 - Withdraw            4 - Calculate interest on balance
    2 - Deposit             5 - Exit
    3 - Check balance


    >"""))
    if action == 1:
        me.withdraw(int(input('Please enter amount you wish to withdraw: ')))
        banking = input('would you like to make another transaction? [y/n]: ')
    if action == 2:
        me.deposit(int(input('Please enter amount you wish to deposit: ')))
        banking = input('would you like to make another transaction? [y/n]: ')
    if action == 3:
        print(me.balance)
        banking = input('would you like to make another transaction? [y/n]: ')
    if action == 4:
        print('This feature has yet to be added.')
    else:
        print('Have a nice day! Goodbye.')
        banking = 'n'
