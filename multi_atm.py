# Multi ATM
# Your task
# Develop a simple banking system in Python that allows users to create an account, deposit funds, withdraw money, 
# and check their balance.

# This time, support multiple accounts.

# Instructions
# Create a command-line application that simulates multiple user banking operations.

# The system should offer a menu with options to perform various transactions and maintain the account balance during the session.

# When the program starts, the user will have to type their credit card number (8 digits), and their PIN (4 digits).

# Then they will log into their account.

# The options inside the account are:

# Deposit money:
# The user will be asked to enter the amount to deposit.
# Withdraw money:
# The user will be asked to enter the amount to withdraw.
# Check if the user has enough funds to withdraw the amount.
# Check balance:
# Display the current account balance.
# Exiting the program:
# Allow user to exit the program.
# Please use the following dictionaries for your program:

# { "12345678": {"pin": "1234", "balance": 100}, }

# { "87654321": {"pin": "4321", "balance": 200}, }

# Approach
# Use a dictionary to represent the different accounts.

accounts = {"12345678": {"pin": "1234", "balance": 100}, "87654321": {"pin": "4321", "balance": 200}}

while True:
    print("Simple Banking System")
    # credit card number (8 digits), and their PIN (4 digits)
    credit_card = input("Enter your credit card number (8 digits): ")
    pin = input("Enter your PIN (4 digits): ")
    if credit_card in accounts and accounts[credit_card]["pin"] == pin:
        print("Login successful.")
        
        while True:
            # Account operation menu
            print("\n1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Select an option (Enter 1, 2, 3, or 4): ")

            if choice == "1":
                # Deposit money
                try:
                    deposit = float(input("Deposit how much? "))
                    if deposit > 0:
                        accounts[credit_card]["balance"] += deposit
                        print(f"Successfully deposited ${deposit:.2f}. Total balance: ${accounts[credit_card]['balance']:.2f}.")
                    else:
                        print("Deposit amount must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif choice == "2":
                # Withdraw money
                try:
                    withdraw = float(input("Withdraw how much? "))
                    if withdraw > 0:
                        if withdraw <= accounts[credit_card]["balance"]:
                            accounts[credit_card]["balance"] -= withdraw
                            print(f"Successfully withdrew ${withdraw:.2f}. Remaining balance: ${accounts[credit_card]['balance']:.2f}.")
                        else:
                            print("Insufficient funds.")
                    else:
                        print("Withdrawal amount must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif choice == "3":
                # Check balance
                balance = accounts[credit_card]["balance"]
                print(f"Current balance is ${balance:.2f}.")

            elif choice == "4":
                print("Logging out.")
                break  # Exit to the main menu for login

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")