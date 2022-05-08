from re import A


a = 1

print(a)

a, b, c = 1, 'Two', 3.0
print(a,b,c)

x, y, z = 1, 1, 1
x = y = z = 3
print(x, y, z)

print(x,y,z, end = "I am done")
print('this is the next line')

# this is how you Single line comment in python with a # 
# Single line comments 


'''
This is how you do Multiple line comment 

'''

"""
This is also how you do multiple line comments
"""
y = 1
z = 32

multiline = '''
    Anything in here is a string 
    even on multiple lines
'''
print(multiline)


# Casting 
m = int(1)
n = str(1)
o = float(1)
p = bool(1)
q = bool('true')
print(m,n,o,p,q)


print(type(m))

# Strings
print('-' * 50)

name = 'Alexander'
fruit = 'Orange'
cost = 1.20 

print (name, fruit, cost)
print(name + fruit + str(cost))
print(name + ' purchased ' + fruit + ' for ' + str(cost) + ' dollars')
# best way to do it below
print(f'{name} purchased {fruit} for {cost} dollars')

together = 'a' 'b' 'c'
print(together)

#length
print(len(together))

l = '       remove spaces     '
l1 = l.strip()
l2 = l.lstrip()
l3 = l.rstrip()
print(l1)
print(l2)
print(l3)


print('-' * 50)
# string indexes
s = 'abcdefg'
print(s[0])
print(s[4])
print(s[len(s) - 1])
print(s[-1])
print(s[0:4])
print(s[0:6:2])
print(s[::-1])