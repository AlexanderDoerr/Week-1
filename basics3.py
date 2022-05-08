# Loops
# For / While
from os import system

i = 1
while True:
    print(i)
    i+=1
    if i > 9:
        break
print('=' * 50)

i = 1 
while i < 10:
    print(i)
    i+=1

#while True:
 #   answer = input('input please: ').lower()
  #  if answer == 'quit':
   #     break

i = 0
while i < 10:
    i+=1
    if i >= 3 and i <= 5:
        continue
    print(i)

print('=' * 50)

i = 1
while i < 6:
    print(i)
    i += 1
    if i > 3:
        break
else:
    print('Out of the Loop')

system('cls')

# For Loops

fruits = ['apple', 'banana', 'cherry']

for f in fruits:
    print(f)

for b in 'bananas':
    print(b)

for t in (1,2,3,4,5):
    print(t)

print()

for i in range(10):
    print(i)

print()

for i in range(2, 8):
    print(i)

print()

for i in range(2, 8, 2):
    print(i)

print()

for i in range(8, 2, -1):
    print(i)

print()

for i in reversed(range(2, 8)):
    print(i)

print()

adj = ['red', 'big', 'Tasty']
frutis = ['apple', 'banana', 'cherry']

for a in adj:
    for f in fruits:
        print(a, f)