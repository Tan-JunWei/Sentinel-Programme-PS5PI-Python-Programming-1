# Create a simple number guessing game where the player tries to guess a randomly generated number within a certain range.

# The program will randomly select a number between 1 and 100 (inclusive).
# The player has limited attempts to guess the number (you can implement selecting easy/medium/hard mode at the game's beginning).
# After each guess, the program should inform the player if their guess is too high, too low, or correct.
# The game ends when the player guesses the correct number.
# Hint
# The generate a random number, use:

# import random

# random.randint(1, 100)

import random
random_number = random.randint(1,100)
difficulty = input("Difficulty (easy/ medium/ hard): ")
difficulty_dict = {"easy":10,
                   "medium":7,
                   "hard":5}
chosen_difficulty_tries = difficulty_dict[difficulty]
tries = 0

# check if input differs from random number generated
while tries < chosen_difficulty_tries:
    guess = int(input("Guess the number: "))
    tries += 1
    if guess > random_number:
        print("Guess is too high! Try again.")

    elif guess < random_number:
        print("Guess is too low! Try again.")
    
    else:
        print("Guess is correct!")
        break
