# Exercise
# Change the function from the previous exercise to get the name of the user as the first argument, and how many times to print it as the second.

# The function will then print the name multiple times.

# Try calling the function with different names, and see what happens.

# Call the function print_name_multiple_times().

name = input("Input name: ")
num = int(input("Input number of times to print name: "))

def print_name_multiple_times(name, num):
    for i in range(num):
        print(f"Hello {name}")

print_name_multiple_times(name, num)



# previous--------------------

# Exercise
# Change the function from the previous exercise to get the name of the user as an argument, and then print it.

# Try calling the function with different names, and see what happens.

# name = input("Input name: ")

# def print_name(name):
#     print(f"Hello, {name}")

# print_name(name)