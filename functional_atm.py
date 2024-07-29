# Functional ATM
# You task
# Develop a simple banking system in Python that allows users to create an account, deposit funds, withdraw money, and check their balance.

# Use functions to simplify your code.

# Instructions
# Create a command-line application that simulates multiple user banking operations.

# The system should offer a menu with options to perform various transactions and maintain the account balance during the session.

# When the program starts, there will be 2 options:

# Create account: Create a new account. Generates a random card number, and let the user choose a secret PIN.
# Login: the user will have to type their credit card number (8 digits), and their secret PIN (4 digits).
# The options inside the account are:

# Deposit money: Allow the user to add funds to their account.
# Withdraw money: Enable the user to withdraw funds, ensuring the account has sufficient balance.
# Check balance: Provide the current account balance.
# Exit: Offer an option to exit the banking system. It will return to the login menu.
# Approach
# Use a dictionary to represent the different accounts.

# Use functions to perform the different operations.
import random

accounts = {"12345678": {"pin": "1234", "balance": 100}, "87654321": {"pin": "4321", "balance": 200}}

def authentication():
    credit_card = input("Enter credit card number: ")
    PIN = input("Enter PIN: ")
    success = False
    if credit_card in accounts and accounts[credit_card]["pin"]:
        print("Login successful!")
        success = True
    else:
        print("Wrong credential input.")
    return success, credit_card

def create_account():
    account_number = str(random.randint(000000000,99999999))
    pin = input("Enter PIN (4 digits): ")
    accounts[account_number] = {"pin":pin,"balance":0}
    print(f"Account {account_number} has been succesfully created.")
    print(accounts)
    return account_number

def deposit_funds():
    success, account = authentication()
    if success:
        deposit = int(input("How much to deposit? "))
        accounts[account]["balance"] += deposit
        print(f"${deposit} has been deposited. Account balance is: ${accounts[account]['balance']}.")
    return accounts[account]['balance'] if success else None

def withdraw_funds():
    success, account = authentication()
    if success:
        amount = int(input("How much to withdraw? "))
        if amount <= accounts[account]['balance']:
            accounts[account]['balance'] -= amount
            print(f"${amount} has been withdrawn. Account balance is: ${accounts[account]['balance']}.")
        else:
            print("Insufficient funds.")
    return accounts[account]['balance'] if success else None

def check_balance():
    success, account = authentication()
    if success:
        print(f"Account balance is: ${accounts[account]['balance']}.")
    return accounts[account]['balance'] if success else None

while True:
    print("Options:")
    print(
        "1. Create account\n"
        "2. Deposit funds\n"
        "3. Withdraw money\n"
        "4. Check balance\n")
    option = input("Choose option (Enter 1, 2, 3 or 4): ")
    if option == "1":
        create_account()
    elif option == "2":
        deposit_funds()
    elif option == "3":
        withdraw_funds()
    elif option == "4":
        check_balance()
    else:
        print("Enter appropriate input.\n")
