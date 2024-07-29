# Exercise
# Write a function that gets the user's favorite color, favorite animal, and favorite food 
# and returns them as multiple values.

def favourites():
    color = input("Favourite color: ")
    animal = input("Favourite animal: ")
    food = input("Favourite food: ")

    return color, animal, food
print(favourites())
