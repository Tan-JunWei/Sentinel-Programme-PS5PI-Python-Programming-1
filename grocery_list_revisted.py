# The program will start with an empty list, and display a menu with support for:

# adding groceries
# removing groceries
# displaying all of the groceries
# importing an existing grocery list from a file
# exporting the grocery list to a file
# exit
# The program will run in a loop until exit.

# Example run
# Grocery List Manager
# 1. Add Groceries
# 2. Remove Groceries
# 3. Display Groceries
# 4. Import Grocery List from File
# 5. Export Grocery List to File
# 6. Exit
# Select an option: 1
# Enter the item to add: pineapple
# 'pineapple' has been added to the list.

# Grocery List Manager
# 1. Add Groceries
# 2. Remove Groceries
# 3. Display Groceries
# 4. Import Grocery List from File
# 5. Export Grocery List to File
# 6. Exit
# Select an option: 3

# Grocery List:
# - pineapple

# Grocery List Manager
# 1. Add Groceries
# 2. Remove Groceries
# 3. Display Groceries
# 4. Import Grocery List from File
# 5. Export Grocery List to File
# 6. Exit
# Select an option: 2
# Enter the item to remove: pineapple
# 'pineapple' has been removed from the list.

# Grocery List Manager
# 1. Add Groceries
# 2. Remove Groceries
# 3. Display Groceries
# 4. Import Grocery List from File
# 5. Export Grocery List to File
# 6. Exit
# Select an option: 5
# Enter the path to export the grocery list: my_grocery_list.txt
# Grocery list exported successfully.

import os

grocery_list = ["pineapple"]

def display_menu():
    print("Grovery List Manager")
    print("1. Add Groceries")
    print("2. Remove Groceries")
    print("3. Display Groceries")
    print("4. Import Grocecy List from File")
    print("5. Export Grocery List to File")
    print("6. Exit")

while True:
    display_menu()
    option = input("Select an option: ")

    if option == "6":
        break

    elif option == "1":
        item = input("Enter the item to add: ")
        grocery_list.append(item)
        print(f"'{item}' has been added to the list.\n")

    elif option == "2":
        item = input("Enter the item to add: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"'{item}' has been removed from the list.\n")
        else:
            print(f"'{item}' not found in grocery list.\n")
    
    elif option == "3":
        print("\nGrocery List:")
        for item in grocery_list:
            print(f"- {item}")
        print()
    
    elif option == "4":
        file = input("Enter the path to import the grocery list from: ")
        if os.path.exists(file):
            with open(file,"r") as file:
                for line in file:
                    grocery_list.append(line.strip())
            print('Grocery list imported successfully')
        else:
            print('No such file found.')
    
    elif option == "5":
        file = input("Enter the path to export the grocery list to: ")
        try:
            with open(file, "w") as file:
                for item in grocery_list:
                    file.write(item + "\n")
            print('Grocery list exported successfully.')
        except Exception as e:
            print(f"An error occurred: {e}")

    else: 
        print("Invalid option")

