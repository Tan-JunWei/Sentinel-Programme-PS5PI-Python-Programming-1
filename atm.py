# ATM
# You task
# Develop a simple banking system in Python that allows users to create an account, deposit funds, withdraw money, and check their balance.

# Instructions
# Create a command-line application that simulates basic banking operations.

# The system should offer a menu with options to perform various transactions and maintain the account balance during the session.

# The options are:

# Create an account: Initialize an account with a starting balance of $0. Ensure that all functions are met with "you did not create an account" if users tried to deposit, withdraw or check balance without creating an account
# Deposit money: Allow the user to add funds to their account.
# Withdraw money: Enable the user to withdraw funds, ensuring the account has sufficient balance.
# Check balance: Provide the current account balance.
# Exit: Offer an option to exit the banking system.
# To submit
# Your code and ensure that the file is submitted with the name "atm.py".

# Expected output
# Default Menu
# Simple Banking System
# 1. Create an Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Check Balance
# 5. Exit
# Select an option: 
# Simple Banking System
# 1. Create an Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Check Balance
# 5. Exit
# Select an option: t
# Invalid option. Please choose again.
# Deposit Function
# Simple Banking System
# 1. Create an Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Check Balance
# 5. Exit
# Select an option: 2
# Enter amount to deposit: 100
# $100.0 deposited.
# Withdraw
# Simple Banking System
# 1. Create an Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Check Balance
# 5. Exit
# Select an option: 3
# Enter amount to withdraw: 100
# Invalid amount or insufficient funds.

account = {"Jordan":530}

while True:
    print("Simple Banking System")
    print("1. Create an account\n"
        "2. Deposit Money\n"
        "3. Withdraw Money\n"
        "4. Check Balance\n"
        "5. Exit")
    choice = input("Select an option (Enter 1, 2, 3, 4 or 5): ")

    if choice == "1":
        name = input("Name: ")
        account[name] = 0
        print(f"{name}'s account has now been created. Balance: ${account[name]}.")

    elif choice == "2":
        name = input("Name: ")
        deposit = int(input("Deposit how much? "))
        for key, value in account.items():
            total = account[name] + deposit # add deposit to existing account
        print(f"Successfully deposited ${deposit}. Total balance: ${total}.")

    elif choice == "3":
        name = input("Name: ")
        withdraw = int(input("Withdraw how much? "))
        for key, value in account.items():
            total = account[name]
        # add deposit to existing account
        if withdraw > total:
            print("Insufficient funds found.")
        else:
            remaining = total - withdraw
            print(f"Successfully withdrew ${withdraw}. Remaining balance: ${remaining}.")

    elif choice == "4":
        name = input("Name: ")
        for key,value in account.items():
            balance = account[name]
        print(f"Current balance is ${balance}")
    
    elif choice == "5":
        break

