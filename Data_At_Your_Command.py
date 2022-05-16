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

    print(f'Successful {person["firstname"]} {person["lastname"]} was added')  
        

def list():
    with open('db.json', 'r')as file2:
        listRecords = json.load(file2)
        for x in listRecords:
            print(f'\n\n{x["firstname"]} {x["lastname"]}, {x["phone"]} \n\n {"-" * 50}')


def find(value):
    with open('db.json', 'r') as file:
        data_json = json.load(file)

        for x in data_json:
            if x['firstname'].lower() == value or x['lastname'].lower() == value:
                print(f'{x["firstname"]} {x["lastname"]}, {x["phone"]}')
                index = data_json.index(x)
        return index
                


def delete(value):
        with open('db.json', 'r') as file:
            new_data_json = json.load(file)
            index = find(value)
            print('Has been deleted')
            del new_data_json[index]

        with open('db.json', 'w') as file2:
                json.dump(new_data_json, file2, indent=4)            

while True:
    commandLine = input('>>> ')
    try:
        values = commandLine.split()
        command = values[0]
        args = values[1:]

        match command.lower():
            case 'add':
                add(args[0], args[1], args[2])
            case 'list':
                list()
            case 'find':
                find(args[0].lower())
            case 'del':
                delete(args[0].lower())
            case 'help':
                print(f'{menu} \n for add "First Name, Last Name, Phone Number" \n value for del and find means either First or Last Name') 
            case 'quit':
                break
            
    except:
        print('Error in entering in information, Please try again')

