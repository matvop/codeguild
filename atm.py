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
# Implement a user interface that lets a user pick each of those actions and updates the account. After each action it will print the balance.
#
# Advanced
#
# Save the account balance to a file after each operation. Read that balance on startup so the balance persists across program starts.
# Add to each account class an account ID number.
# Allow the user to open more than one account. Let them perform all of the above operations by account number.
import os
class Account:
    def setup(self, name, balance):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

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

os.system('cls')
user_list = []
user_list.append(int(input('Please enter your 3 digit account number: ')))
user_list[0] = Account()
user_list[0].setup('Matt', 0)
banking = 'y'
"""create a dict for storage of user's name, balance, and account#. This information should be saved to an external txt."""
while banking.lower() == 'y':
    os.system('cls')
    print('Welcome {}, would you like to withdraw or deposit funds?'.format(user_list[0].name))
    action = int(input("""
    1 - Withdraw
    2 - Deposit

    >"""))
    if action == 1:
        user_list[0].withdraw(int(input('Please enter amount you wish to withdraw: ')))
        banking = input('would you like to make another transaction? [y/n]: ')
    if action == 2:
        user_list[0].deposit(int(input('Please enter amount you wish to deposit: ')))
        banking = input('would you like to make another transaction? [y/n]: ')
    else:
        print('Have a nice day! Goodbye.')
        banking = 'n'
