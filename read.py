file_path = input("Enter file path: ")

with open(file_path,'r') as file:
    content = file.read()
    print(content)