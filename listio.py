import os 

path = './images/'

if not os.path.exists(path):
    os.makedirs(path)

files = os.listdir(path)

for image in files:
    if image.endswith('.jpg'):
        print(files)

#list comprehension
images = [file for file in files if file.endswith('.jpg')]
print(images)



