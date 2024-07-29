# Instructions
# Input
# A target word (string)
# A list of words (string)
# Functionality
# Your Python script should perform the following tasks:

# Allow input of target word
# Allow input of word list
# Iterate through each word in the word list.
# Check if the length of the current word matches the length of the target word.
# If the lengths match, check if the current word is an anagram of the target word.
# Print a list of all words from the input list that are anagrams of the target word.
# Your anagram function should be sensitve to capital letters ( Example: "Listen" is NOT an anagram of "silent")
# Example
# If the target word is "listen" and the list of words is ["enlist", "silent", "hello", "world", "tinsel", "banana"], the script should 
# print ["enlist", "silent", "tinsel"].

# Example Output
# Input your target word: listen
# Input your word list: enlist silent hello world tinsel banana 
# These are the anagrams: ['enlist', 'silent', 'tinsel']

target_word = input("Input your target word: ")
word_list = input("Input your word list: ")
anagrams = []

# make chars in word into a list, then sort
char_in_target = list(target_word)
char_in_target.sort()

for word in word_list.split():
    # make chars in word into a list, then sort
    char_list = [x for x in word]
    char_list.sort()

    # check criteria
    if char_in_target == char_list:
        anagrams.append(word)

print(f"These are the anagrams: {anagrams}")