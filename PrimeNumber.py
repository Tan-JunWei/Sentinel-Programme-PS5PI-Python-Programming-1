import math

num = int(input("Enter a number: "))
primes = []

for i in range(2,num):
    prime = True
    for j in range(2,math.floor(math.sqrt(i))+ 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        primes.append(i)

print(primes)