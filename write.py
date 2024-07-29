import os

string_to_add = input("Please enter the string you want to write to the file: ")
file_path = input("Please enter the file path where you want to write the string: ")

if os.path.isfile(file_path):
    with open(file_path,'w') as file:
        file.write(string_to_add)
        print(f"The string has been written to {file_path}")

else: 
    print("No file found.")