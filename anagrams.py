# Implement the function find_anagrams(word_list) to find words that are anagrams.

# Description
# Write a function find_anagrams(word_list) that takes in a list of strings and partitions the list such that each partition is a 
# list of anagrams. All the words that are not anagrams are not included in the output. If there are no anagrams present, return an empty list.

# Here is an example of what the return might look like:

#     >>> find_anagrams(['deltas', 'desalt', 'lasted', 'salted', 'banana'])
#     [['deltas', 'desalt', 'lasted', 'salted']]

#     >>> find_anagrams(['xyz', 'xyz', 'deltas', 'desalt', 'lasted', 'salted', 'corns', 'scorn'])
#     [['deltas', 'desalt', 'lasted', 'salted'], ['corns', 'scorn']]

#     >>> find_anagrams([["aBc", "cAb", "baC"]])
#     [["aBc", "cAb", "baC"]

word_list = ['deltas', 'desalt', 'lasted', 'salted', 'banana']

def find_anagrams(word_list):
    anagrams = {}

    for word in word_list:
        anagram_word = "".join(sorted(word.lower()))
        
        if anagram_word not in anagrams:
            anagrams[anagram_word] = [word]
        else:
            anagrams[anagram_word].append(word)

    print([words_list for words_list in anagrams.values() if len(words_list) > 1])

find_anagrams(word_list)
