'''
questions = [
    {"question" : "What is the area of Singapore (in square km)?",
     "options" : ["102", "1503", "842", "734"],
     "correct_index" : 3
    },
    {"question" : "What is the capital of France?",
     "options" : ["London", "Paris", "Barcelona", "New York"],
     "correct_index" : 1
    }
]
'''
from questions import questions

# initialise the number of correct ans
correct = 0

for i in range(len(questions)):
    # obtain actual question from the dictionary
    actual_qn = questions[i]["question"]
    print(f"Question: {actual_qn}")
    
    # for loops is used to show the possible options for the MCQ
    for x in range(len(questions[i]["options"])):
        print(f"{x+1}. {questions[i]["options"][x]}")
    answer = input("Your answer: ")

    # check if user has input correct answer
    if answer == str(questions[i]["correct_index"]+1):
        print("Congratulations! You are correct!\n")
        correct +=1 # +1 to correct counter if correct answer is given
    else:
        print("Wrong answer...try again?")

print(f"Total correct answers: {correct}")