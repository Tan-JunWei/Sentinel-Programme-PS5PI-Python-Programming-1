# Exercise
# Write a function that gets a list of numbers as an input, and returns their average.

# Test it.

# num_list = 5 10 15 20 25
num_list = input("List of numbers: ")
num_list = [int(x) for x in num_list.split()]
def average_list(num_list):
    average = sum(num_list) / len(num_list)
    return average

print(average_list(num_list))