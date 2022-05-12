from enum import unique
from os import system
# Dictionaries

list1 = []
tuple1 = ()
dict1 = {'key':'value'}

dict2 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
    
    'favorite': True,
    'colors': ['red', 'blue'],
    1: '4 Wheels'
}

print(dict2)
print(dict2['brand'])
dict2['model'] = 'Thunderbird'

print(dict2)
print(len(dict2))

print('-' * 50)

dict3 = dict()
dict3['name'] = 'Scott'
dict3['age'] = 25

print(dict3)

print('-' * 50)

cars = [
    {'brand':'Toyota', 'model':'Mustang', 'year':1964},
    {'brand':'Honda', 'model':'Prelude', 'year':1989},
    {'name':'Alex', 'age':24}
]
print(cars)

system('cls')

# Sets

set1 = {'apple', 'banana', 'orange', 'banana'}

print(set1)

list1 = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,34]
set1 = set(list1)
list1 = list(set1)
print(list1)

list1 = list(set([1,1,1,1,1,2,2,2,2,3,3,3,3,3,34]))
print(list1)

u = set('Hello, my name is Alex')
print(u)

# Union and Intersection 
a = {1,2,3}
b = {3,4,5}
print(a.union(b))
print(a.intersection(b))