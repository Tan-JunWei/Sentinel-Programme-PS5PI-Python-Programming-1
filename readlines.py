# Exercise
# Read the ancient_scroll.txt file using the readlines function, and do as the instructions above say.

# He found it along with the following instructions:

# Take the second word of the first line.
# Then, find the next line that contains this word.
# Take the last word in that line.
# Then, find all of the next lines that contain this word. Those are the lines you should print.

with open("ancient_scroll.txt","r") as file:
    lines = file.readlines()
    first_line = lines[0]
    first_line_words = first_line.split() # make a list containing words in first line
    second_word_in_first_line = first_line_words[1]
    next_line_with_second_word = ""

    for line in lines[1:]: #first line onwards
        if second_word_in_first_line in line:
            index = lines.index(line)
            next_line_with_second_word += line.strip()
            break

    # print(next_line_with_second_word)

    words_in_next = next_line_with_second_word.split() # get a list containing words from the next line
    final_word = words_in_next[-1] # find final word
    
    for line in lines[index+1:]: # next lines, thus index + 1
        if final_word in line:
            print(line)