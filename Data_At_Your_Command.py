import json

menu = '''
Please type what you would like to do

        add [LName][FName][Phone]    (add a new contact record)

        list                         (list all records)

        find [value]                 (find and show the first record that matches the search)

        del [value]                  (delete the first record that matches the search)

        help                         (Shows what is needed for each option)

        quit                         (quit the CLI)
'''



print(menu)

people = []

def add(FirstName, LastName, Phone):
    
    person = {'firstname':FirstName, 'lastname':LastName, 'phone':Phone}
    people.append(person)

    with open('db.json', 'w') as file1:
        json.dump(people, file1, indent=4)

    print(f'Successful {person} was added')  
        

def list():
    with open('db.json', 'r')as file2:
        listRecords = json.load(file2)
        for x in listRecords:
            print(f'{x} \n')


def find(value):
    with open('db.json', 'r') as file:
        data_json = json.load(file)

        for x in data_json:
            if x['firstname'] == value or x['lastname'] == value:
                print(x) # you can make it look nicer
                return x
                


def delete(value):
        # bob = find(value)
        # del bob[value]

         with open('db.json', 'w') as file:
            data_json = json.load(file)

            for x in data_json:
                if x['firstname'] == value or x['lastname'] == value:
                    del  x    # x is not the actual index number but the actual dictionary                 

while True:
    commandLine = input('>>> ')
#try:
    values = commandLine.split()
    command = values[0]
    args = values[1:]

    match command.lower():
        case 'add':
            add(args[0], args[1], args[2])
        case 'list':
            list()
        case 'find':
            find(args[0])
        case 'del':
            delete(args[0])
        case 'help':
            print(f'{menu} \n for add "First Name, Last Name, Phone Number" \n value for del and find means either First or Last Name') 
        case 'quit':
            break
        
#except:
    #print('Error in entering in information, Please try again')

