"""                JSON => JAVASCRIPT OBJECT NOTATION                """
"""
it is data format for storing & exchanging some information among other applications.
Inspired by javascript
Every language has libraries for parsing and generating json data.

Its main purpose is to transfer data / objects from client to server or from one type of
application to another.

Used for fetching data from online APIs.
in used mostly webservices and its extension is ".json"

Json format looks like python dictionery.

where keys always enclosed in double quotes.


In python json data is represented as string. we can use 'json' module to perform json operations


To convert python to json:-
1. dumps() -> does not create file.
2. dump() -> creates a file.
"""

import json

d = {'name' : 'sushil', 'age' : 25, 'ismarried' : False, 'insurance' : None} 

name = "Sushil"
age = "25"
data = ["Sushil", 22, False , None]
data1 = ("Sushil", 22, False , None)
var = None


# converting above py data to json
# print(json.dumps(d))
# print(type(json.dumps(d)))

# print(json.dumps(data))
# print(json.dumps(data1))
# print(json.dumps(var))


py_data = {
    'Age' : 22,
    'City' : 'Mumbai',
    'Name' : 'Sushil',
    "Number" : 9326547896,
    "Subject" : [
        'Python',
        'Javascript',
        'Django Rest Framework',
        'React js',
        'Django'
    ],
    'IsMarried' : False
}

# json_data = json.dumps(py_data, indent=4, separators= (';', "||"), sort_keys=True)

# f = open('data.json', mode='w')
# json_data = json.dump(py_data,f, indent=4, sort_keys=True)    #creates file
# print(json_data)
# print(type(json_data))






"""
*to convert json data to python:-
1. loads :- doesn't create file
2. load  :- creates shareable file.

"""


py_data = {
    'Age' : 22,
    'City' : 'Mumbai',
    'Name' : 'Sushil',
    "Number" : 9326547896,
    "Subject" : [
        'Python',
        'Javascript',
        'Django Rest Framework',
        'React js',
        'Django'
    ],
    'IsMarried' : False
}

#py to json conversion :-
json_data = json.dumps(py_data)
# print(json_data)
# print(type(json_data))


# json to py(dict) conversion :-
# data1 = json.loads(json_data)
# print(data1)
# print(type(data1))   #python dict format 








def salary_credit():
    f = open('data1.json', mode='r')
    data_dict = json.load(f)    #to read json to py
    # print(data_dict['Employees'])
    for key in data_dict['Employees']:
        # print(data_dict['Employees'][key])
        if data_dict['Employees'][key]['Bank_name'] == "Bank of Maharashtra":
            print("Process salary")
            print(f"Salary {data_dict['Employees'][key]['Salary']} processing in {data_dict['Employees'][key]['Name']}'s account")

    f.close()
    
# salary_credit()