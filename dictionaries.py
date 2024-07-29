# Exercise
# Write a program that asks the user for a student’s name. The program will print the grade of this student. Please use 
# the dictionary from the example above.

# Follow the input and output flow:

# Example 1:

# Enter a student's name: Laura
# The student's grade is: 65
# If the student’s name doesn’t exist, print an error message.

# Hint: Use dict.get
# Example 2:

# Enter a student's name: Timothy
# Error: student not found.

student_name = input("Enter a student's name: ")
students_dict = {"Mark": 80, "David": 90, "Laura": 65, "Johanna": 100}

marks = students_dict.get(student_name)

if marks: 
    print(f"The student's grade is: {marks}")
else:
    print("Error: student not found.")