# Instructions
# Your program should accept a string input representing the phrase for which an acronym needs to be generated. 
# (Avoid inputting special characters such as "&", "@" etc.)

# The program should print the generated acronym all in capital letters (inclusive of letters such as "of", "and", "the" etc.)

# Example Output
# Enter the phrase to generate an acronym: Ministry Of Manpower
# Acronym: MOM

strng_form = input("Enter the phrase to generate an acronym: ")
strng_list = strng_form.split()
acronym = ""

for word in strng_list:
    first_char = word[0]
    if first_char.isalpha():
        first_char = first_char.capitalize()
        acronym += first_char

print(f"Acronym: {acronym}")
