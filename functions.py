# Function

def my_function(value1, value2=-1, value3=-1):
    if value1 != -1 and value2 != -1:
        return f'The values are {value1}, {value2}'
    else:
        return "No values passed"  
print(my_function(value1=1, value2=2))

print('-' * 50)

#Convert into tuple
def my_function2(*kids):
    print(f'you passed {len(kids)} parameters')
    print(kids)
    print(f'The first kid is {kids[0]}')

my_function2('Tom', 'Sally', 'Bruce')

print('-' * 50)

#Convert into Dictionary
def my_function3(**kids):
    print(kids)

my_function3(kid1='Tom', kid2='Sally', kid3='Bruce')

print('-' * 50)

def my_function4(value):
    value.append('changed')

age = [25]
my_function4(age)
print(f'My age is {age}')

# Global Variabes
my_global = 1

def add_one():
    other_number = 10
    global my_global
    my_global += 1
    print(f'my_global = {my_global}')

add_one()
print(my_global)

print('-' * 50)

# Recursion

loops = 0 
def try_recursion(value):
    global loops
    loops += 1
    
    print(f'looping: {loops}')
    if value > 0 :
        result = value + try_recursion(value - 1)
        print(result)
    else:
        result = 0 
    return result

try_recursion(3)




