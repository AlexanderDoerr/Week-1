from ast import Constant, match_case
from os import system
from pickle import TUPLE
# String

abc = 'a b c d e g f'
letters = abc.split()
print(letters)

abc = 'a,b,c,d,e,g,f'
letters = abc.split(',')
print(letters)

j = ":".join(letters)
print(j)

# replace
t = 'I saw the old man by the sea. old, old, old'
t1 = t.replace('old', 'young')
t2 = t.replace('old', 'young', 1)
print(t1)
print(t2)

# Find
fruits = 'apple banana orange banana'
print(fruits.find('banana'))
print(fruits.rfind('banana'))
print(fruits.find('banana', 10))
f1 = fruits.split()

system('cls')

# List
myList = ['apple', 'banana', 'cherry', 'peach', 'banana', 1, True, 192.88]

print(myList[1])
myList[1] = 'pear'
print(myList)

print(myList[:2]) # : will start at 0 then whatever number you specify after will go up to 
print(myList[1:3]) # : will start at 1 then whatever number you specify after will go up to  
print(myList[::-1]) 

myList.append('New')
print(myList)

myList.pop()
print(myList)
myList.pop(1)
print(myList)
myList.remove('peach')
print(myList)
del myList[0]
print(myList)

# Initialize a list
l = []
l.append(True)

l2 = list()


system('cls')

# Searching list
myList = ['apple', 'banana', 'cherry', 'peach', 'banana', 1, True, 192.88]
print(myList.index('banana'))
print(myList.index('banana', 2))
print(myList.count('banana'))
print('peach' in myList)
print('peach' not in myList)
print('peach2' in myList)
print('peach2' not in myList)

# Copy a list memory location
myList = ['apple', 'banana', 'cherry', 'peach']
myListCopy = myList # copy memory address
print(myList)
print(myListCopy)
myList.append('pear')
print(myList)
print(myListCopy)
print('-' * 50)

# Copy a list for real
myList = ['apple', 'banana', 'cherry', 'peach']
myListCopy = myList.copy()
print(myList)
print(myListCopy)
myList.append('pear')
print(myList)
print(myListCopy)

system('cls')


# Tuples
t1 = tuple()
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tuple1[0])

tuple2 = 1,2,3,4,5,1,2,3,4,5 # allows duplicate values
print(tuple2)

tuple3 = ('Scott', 1, True)
print(tuple3)

not_a_tuple = ('No') # this is just a value since there is only one value
print(not_a_tuple)

is_a_tuple = ('Yes',)
print(is_a_tuple)

# Unpacking a tuple / might be useful for assignment
tuple4 = ('Name', 10, True)
v1, v2, v3 = tuple4
print(v1, v2, v3)

# List of Tuples
l = [
    ('Question 1', 1),
    ('Question 2', 2)
]

print(l[0])
print(l[0][0])

system('cls')

# Conditoinals
print (1 < 2)
print( 1 > 2)
print( 1 >= 2)
print( 1 <= 2)
print(1 == 2)
print(1 != 2)

if 1 < 2:
    print('This statement is true')
    print('This statement is true 2')
    print('This statement is true 3')
else:
    print('This statement is false')
    print('This statement is false 2')
    print('This statement is false 3')

a = 1
b = 2
min = a if a < b else b

a = 1
b = 2
c = 3
if a < b:
    print(f'{a} is less than {b}')
elif b < c:
    print(f'{b} is less than {c}')
else:
    print(f'{a} is not less than {b} which is not less{c}')


a = 5
b = 4
c = 3

if a > b and b > c:
    print("Yes")

if a > b or c > b:
    print('Yes')

if a > b:
    pass

