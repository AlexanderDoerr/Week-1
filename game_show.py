import random 
from os import system

questions = [
    ('What is your favorite color:', 'yellow', ['red', 'blue', 'yellow', 'green']),
    ('What is your favorite car:', 'mazda', ['honda', 'mazda', 'toyota', 'cheverlet']),
    ('What is your favorite food:', 'cherry', ['apple', 'banana', 'orange', 'cherry'])
]

random.shuffle(questions)
try:
    for q in questions:
        system('cls')
        random.shuffle(q[2])
        print(q[0])
        i = 1
        for a in q[2]:
            print(f'{i}) {a}')
            i += 1
        answer = input('What is your answer please: ')
        answer = int(answer)
        

        if q[2][answer-1] == q[1]:
            print('You are correct')
        else:
            print('Wrong. You lose!')
            break
        print()
        input('Hit enter for the net question')

except:
    print("Invalid input. Please try again")
