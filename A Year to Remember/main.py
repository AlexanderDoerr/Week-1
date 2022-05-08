#Import Random
import random
#Build the Tuples with Questions

Questions = [
    ('the start of the Revolutionary War', 1775),
    ('the United States constitution signed', 1783),
    ('President Lincoln assassinated', 1865),
    ('Theodore Roosevelts first day in office sa President of the United States', 1901),
    ('the beginning of World War II', 1939),
    ('the first personal computer introduced', 1975),
    ('the Berlin Wall taken down', 1989),
    ('the coolest person was born', 1997),
    ('the terror attack that happened on 9/11 in the US', 2001),
    ('the first moon landing', 1969)
]

random.shuffle(Questions)
score = 0

try:
    for x in Questions:
        question = x[0]
        correctAnswer = x[1]
        userInput = input(f"In what year was {question}?")
        inputInt = int(userInput)
        if inputInt == correctAnswer:
            score+=10
            print(f'Correct! You got 10 points, Score is now {score}.')
        elif input > correctAnswer:
            print{}
except:
    print("Invalid input Please try again")





# Have validation 
def UserInt():
    iTemp = 0
    date = input("What is the date?")
    while iTemp <= 0:
        try:
            iTemp = date
        except:
            print("Please enter a valid date")
        else:
            return iTemp





