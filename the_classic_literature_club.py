# The Classic Literature Club
# You have been tasked by the Classic Literature Club to analyze famous texts and determine the most prominent words used by 
# legendary authors.

# Your program will read a passage or a file containing a piece of classic literature, count the frequency of each word, and exclude 
# common stopwords to highlight the unique vocabulary of the author.

# Instructions
# Develop a program to analyze the frequency of words in classic literature, excluding common stopwords, to uncover the unique vocabulary
# of legendary authors.

# Input
# Accept a path to a text file containing the literary passage.
# Ensure the analysis is case-insensitive.
# Processing
# Analyze the text to count the frequency of each word.
# Exclude common stopwords ("the", "is", "in", "and") to focus on meaningful words.
# Output
# Store word counts in a dictionary with words as keys and their frequencies as values.
# Display
# Implement functionality to display the top N most frequent words.
# Test
# Test your code on the attached excerpt from the classic Shakespeare play "Hamlet".
import string

file_path = input("Enter path to text file containing literary passage: ").lower()
limit = int(input("Enter n: "))
stopwords = ["the", "is", "in", "and"]

with open(file_path, "r") as file:
    text = file.read().lower()
    
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)

    words = text.split() # make each word into a list

    word_counts = {}
    for word in words:
        if word not in stopwords:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

# print(word_counts)                

def most():
    sorted_count = sorted(word_counts.items(), key = lambda item: item[1], reverse = True) # sort according the frequency

    # check if limit is appropriate
    if limit < len(sorted_count):
        # print top n words with highest frequency
        print(f"Top {limit} words with highest frequency: ")
        for i in range(limit):
            print(f"{i+1}. {sorted_count[i][0]} ({sorted_count[i][1]} times)")
    else:
        print("Invalid n.")

most()
