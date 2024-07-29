# Little Arithmetics
# Create a new python file that will serve as a module.

# In this module, provides functionalities for basic mathematical operations such as addition, subtraction, 
# multiplication, and division.

# Create a main module that imports those functions and tests them.

# Instructions
# Module Structure
# Your Python module should contain the following functions:

# add: Takes two numbers as input and returns their sum.
# subtract: Takes two numbers as input and returns their difference.
# multiply: Takes two numbers as input and returns their product.
# divide: Takes two numbers as input and returns their quotient. Make sure to handle division by zero gracefully.
# Implementation
# Implement each function to perform the specified mathematical operation.
# Ensure proper input validation and error handling, especially for division by zero.
# Provide clear and concise documentation for each function explaining its purpose and usage.
# Testing
# Test your module by importing it into a separate Python script.
# Call each function with different input values to verify its correctness.
# Use selective import (from math_operations import add, subtract, multiply, divide)
# Handle any errors or edge cases gracefully.

'''
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return "invalid! Cannot divide by zero"
'''

from module import add, subtract,multiply, divide

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply or divide): ")

if operation.lower() == "add":
    print(f"The sum of {x} and {y} is {add(x,y)}.")
elif operation.lower() == "subtract":
    print(f"When {y} is subtracted from {x}, the result is {subtract(x,y)}.")
elif operation.lower() == "multiply":
    print(f"The product of {x} and {y} is {multiply(x,y)}.")
elif operation.lower() == "divide":
    print(f"The result of {x} divided by {y} is {divide(x,y)}.")
else:
    print("Enter one of the four operations above.")
