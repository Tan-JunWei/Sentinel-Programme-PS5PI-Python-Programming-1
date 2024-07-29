# Exercise
# King Kahuka has a French to Portugese dictionary, and he wants to reverse it - 
# have a Portugese to French dictionary.

# Write a code that takes a dictionary, and reverses it - the key will be the values, and vice versa.

# Bonus: if more than one key have the same value, the new value will be a list of the old keys.

# Initialize an empty dictionary to store the reversed dictionary
dict = {1: "one", 2: "two", 3: "two", 4: "four", 5: "five"}
reversed_dict = {}

for key in dict.keys():
    if dict[key] in reversed_dict.keys():
        reversed_dict[dict[key]] = [reversed_dict[dict[key]], key]
    else:
        reversed_dict[dict[key]] = key
print(reversed_dict)

# {'one': 1, 'two': [2,3], 'four': 4, 'five': 5}