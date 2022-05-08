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
        absoluteValue = abs(inputInt - correctAnswer)

        if absoluteValue == 0:
            score+=10
            print(f'Correct! You got 10 points, Score is now {score}.')

        elif absoluteValue <= 5:
            score+=5
            print(f'You were so close! You were {absoluteValue} years off. The correct answer was {correctAnswer}. You still get 5 points! Your new score is {score}')

        elif absoluteValue <= 10:
            score+=2
            print(f'Incorrect. You were {absoluteValue} years off. The correct answer was {correctAnswer}. You still get 2 points! Your new score is {score}')

        elif absoluteValue <= 20:
            score+=1
            print(f'Incorrect. You were {absoluteValue} years off. The correct answer was {correctAnswer}. You still get 1 point! Your new score is {score}')
        
        else:
            print(f"Incorrect, Your guess was too big and didn't earn any points. You were {absoluteValue} years off, The correct answer was {correctAnswer}")

    print(f"Thank you for playing the Guessing game 'A Year to Remember' your final score was {score}")
except:
    print("Invalid input Please try again")
