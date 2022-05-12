# File I/O Input/Output

# 'r' read = stream in at the beginning of the file
# 'w' Write = stream out at the beginning of the file / will overwrite at the begining of the file if anything is there
# 'a' Append = stream out at the end of the file / will append to the end of whatever is already there

file = open('test1.txt', 'w')
file.write('Hello, world\n')
file.write('Thanks for visiting\n')
file.close()

file1 = open('test1.txt', 'r')
content = file1.read()
file1.close()
print(content)

file2 = open('test1.txt', 'a')
file2.write('and now for something completley different')
file2.close()

with open('test1.txt', 'w') as file3:
    file3.write('I overwrite everthing')
