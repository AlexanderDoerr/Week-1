# Build your own CLI
from os import system
system('cls')

menu = """
You can perform the following actions
    echo [value]            -Returns the input
    add [number] [number]   -Returns the sum of two numbers

    quit                    -Quits the CLI
"""

def echo(value1):
    print(f'This is an echo for {value1}')
    return True

def add(num1, num2):
    result = 0
    try:
        result = int(num1) + int(num2)
    except:
        pass
    return result
    

print(menu)


while True:
    commandline = input('>>> ')

    values = commandline.split()
    command = values[0]
    args = values[1:]

    if command == 'echo':
        if(echo(args)):
            print('Echo Function success')
    elif command == 'add':
        print(add(args[0], args[1]))
    elif command == 'quit':
        print('Thank you for using the CLI')
        exit()
    else:
        print('Please learn to use the CLI correctly')
        print(menu)