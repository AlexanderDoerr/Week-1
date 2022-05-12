# Json
import json

# Python objects and their equivalent conversion to JSON:

#Python         JSON Equivalent
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

emp = {
    "employee": [
        {"name": "Alex", "age": 25},
        {"name": "David", "age": 34}
    ]
}

data = '{"name":"Scott", "Age":21, "type":"Zombie"}'
print(data)

data_json = json.loads(data)
print(data_json)

print(data_json['name'])

string_data = json.dumps(data_json)
print(string_data)

with open('test.json', 'w') as file1:
    file1.write(string_data)

db = [
    {'brand':'toyota', 'model':'corrola'},
    {'brand':'honda', 'model':'civic'}
]

with open('test2.json', 'w') as file2:
    json.dump(db, file2, indent=4)
    
with open('test2.json', 'r') as file3:
    vehicles = json.load(file3)

print(vehicles)
print(len(vehicles))

for v in vehicles:
    print(v['brand'], v['model'])
