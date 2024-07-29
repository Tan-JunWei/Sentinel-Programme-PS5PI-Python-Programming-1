# Instructions
# Input
# The target input to be checked for palindrome properties (string)
# Functionality
# The program should print a message indicating whether the input string is a palindrome or not.

# Example Output
# Example 1:

# Input string: A man, a plan, a canal, Panama!
# Is Palindrome: True
# Example 2:

# Input string: hello my name is sam
# Is Palindrome: False
# Hint
# Read the Python Manual strings documentation.

# Try to find functions that will help you.

strng = input("Input string: ")
letters_in_strng = ""

palindrome = False
for char in strng:
    if char.isalpha():
        letters_in_strng += char.lower()

reversed_letters = letters_in_strng[::-1]

if letters_in_strng == reversed_letters:
    palindrome = True

print(f"Is Palindrome: {palindrome}")
