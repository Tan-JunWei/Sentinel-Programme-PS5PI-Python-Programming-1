# She changed the order of the letters in every word (so ‘hello’ became ‘olleh’), and then she changed every space (’ ’) to a random 
# number (for example, after both of the changes above, “hello make my world” became “olleh2ekam5ym9dlrow”).

# As if that wasn’t enough, the monster then used a substitution cipher, and changed each letter to a different one, using this dictionary:

# {'s': 'L', 'b': 's', 'w': 'O', 'z': 'G', 'c': 'o', 'J': 'y',
# 'V': 't', 'P': 'w', 'B': 'f', 'Z': 'q', 'F': 'k', 'O': 'N',
# 'u': 'A', 'W': 'r', 'K': 'K', 'a': 'D', 'v': 'l', 'g': 'S',
# 'f': 'x', 'x': 'c', 'N': 'e', 'p': 'b', 'U': 'a', 'j': 'P',
# 'o': 'Q', 'i': 'I', 'M': 'd', 't': 'U', 'H': 'V', 'X': 'i', 
# 'Y': 'T', 'R': 'H', 'h': 'X', 'L': 'z', 'G': 'F', 'A': 'W', 
# 'm': 'n', 'T': 'u', 'l': 'B', 'C': 'Z', 'q': 'p', 'D': 'v', 
# 'I': 'g', 'n': 'h', 'y': 'C', 'S': 'j', 'k': 'M', 'd': 'J', 
# 'Q': 'E', 'e': 'Y', 'r': 'R', 'E': 'm'}

# Steps
# Implement both the encrypt() and decrypt() functions
# Add tests in a test() function, using assert and various inputs
# Implement main() function

{'s': 'L', 'b': 's', 'w': 'O', 'z': 'G', 'c': 'o', 'J': 'y',
'V': 't', 'P': 'w', 'B': 'f', 'Z': 'q', 'F': 'k', 'O': 'N',
'u': 'A', 'W': 'r', 'K': 'K', 'a': 'D', 'v': 'l', 'g': 'S',
'f': 'x', 'x': 'c', 'N': 'e', 'p': 'b', 'U': 'a', 'j': 'P',
'o': 'Q', 'i': 'I', 'M': 'd', 't': 'U', 'H': 'V', 'X': 'i', 
'Y': 'T', 'R': 'H', 'h': 'X', 'L': 'z', 'G': 'F', 'A': 'W', 
'm': 'n', 'T': 'u', 'l': 'B', 'C': 'Z', 'q': 'p', 'D': 'v', 
'I': 'g', 'n': 'h', 'y': 'C', 'S': 'j', 'k': 'M', 'd': 'J', 
'Q': 'E', 'e': 'Y', 'r': 'R', 'E': 'm'}

with open("encrypted_string.txt","r") as file:
    for line in file:
        line = line.split("\n")
        print(line)