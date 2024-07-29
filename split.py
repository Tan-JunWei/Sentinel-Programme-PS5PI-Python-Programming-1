# Exercise
# Write a program that gets a string from the user, and prints how many words are in it.

# You can assume that the words are separated by a single space.

# Example Output
# Enter a string: mug straw tesla car wallet headphones
# The number of words in the string is: 6

strng = input("Enter a string: ")
print(len(strng.split()))