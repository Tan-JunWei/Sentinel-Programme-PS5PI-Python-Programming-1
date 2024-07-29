# Zigzag
# Write a Python program that generates a "zigzag" sequence of numbers across multiple rows, based on user input for the
# sequence length and height.

# A zigzag sequence arranges numbers back and forth in a zigzag pattern. For example, a zigzag sequence with a length of 13 
# and a height of 3 could look like this:

# 1       5       9       4
#   2   4   6   8   1   3
#     3       7       2
# Instructions
# Prompt the user for two integers: the length of the sequence and the height of the zigzag pattern.
# Generate and display the zigzag sequence of numbers based on the given length and height.
# Use nested loops to calculate and print the zigzag pattern.
# You may need to determine the position of each number in the grid based on its order in the sequence and the current 
# "direction" of the zigzag (up or down).
# Print out the entire sequence in a zigzag pattern as illustrated above.
# Suggested Approach
# Initialize an empty grid or list of lists to hold the pattern.
# Determine the direction of movement (up or down) for each number based on its position in - the sequence.
# Place each number in its correct position within the grid based on its calculated row and column.

sequence = int(input("Enter length: "))
height = int(input("Enter height: "))

sequence_list = [[' ' for i in range(sequence)] for z in range(height)]

row = 0
direction = 1  # 1 for down, -1 for up
counter = []
temp = 1

for a in range(sequence+1):
    counter.append(a%9 + 1)

for i in range(sequence):
    sequence_list[row][i] = str(counter[i])
    row += direction
    if row == (height-1) or row == 0:
        direction *= -1

for row in sequence_list:
    print("".join(row))

