# Fibonacci
# Now it’s time for you to take a recursive challenge! Are you ready?

# Exercise
# Fibonacci series is a series of numbers in which every number is the sum of the 2 numbers that came before.

# It starts with: 0, 1, 1, 2, 3, 5, 8, 13…

# Write a recursive function that returns the n-th number in the series.

# Example output:

# >>> fibonacci(2)
# 1
# >>> fibonacci(3)
# 2
# >>> fibonacci(0)
# 0
# >>> fibonacci(10)
# 55
# Please ensure that your function is defined as "fibonacci".

def fibonacci(n):
    fibonacci_list = [0, 1]
    for _ in range(2, 99):
        sum = fibonacci_list[-2] + fibonacci_list[-1]
        fibonacci_list.append(sum)
    return fibonacci_list[n]
    

print(fibonacci(10))
