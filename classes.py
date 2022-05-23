

class recipe:
    prop = True

recipe.cookingTime = 30


cookie = recipe()
print(cookie.prop)
print(recipe.cookingTime)
print(recipe.prop)
print('_' * 50)

class animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def speak(self):
        print(f'Hi my name is {self.name} and I am a {self.type}')


dog = animal('Fido', 'Dog')
cat = animal('Tom', 'Cat')

print(dog.name)
dog.speak()
cat.speak()
print('_' * 50)

#Inheritance
class bird():
    def __init__(self):
        print('bird is initialized')
        self.color = 'grey'

    def flight(self):
        print('Most birds can fly but some cannot')

class sparrow(bird):
    def __init__(self):
        super().__init__()
        self.color = 'redish brown'
        print('sparrow is initialized')
        
    def flight(self):
        print('I can fly')
        

class emu(bird):
    def __init__(self):
        super().__init__()
        print('emu is initialized')

    def flight(self):
        print('I will never fly')
        

henry = sparrow()
Bob = emu()

print(henry.color)
henry.flight()
print(Bob.color)
Bob.flight()
    

        
        
        



