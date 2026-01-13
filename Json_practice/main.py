"""
What is JSON in Python?
✅ Best Interview Answer

JSON stands for JavaScript Object Notation.
It is a lightweight text format used for storing and exchanging data.
In Python, JSON is used to serialize objects into a universal format that can be shared across different systems and languages.

Reply done for Theory Q2 😎

 dn

🔥 Smooth — next one!

⭐ Theory Q2
❓ Why do we use JSON instead of Pickle?
✅ Best Interview Answer

JSON is language-independent and readable by any system, not just Python.
Pickle works only inside Python environments and can’t be shared easily.
So JSON is preferred for APIs, web services, and data exchange between different platforms or programming languages.

Reply done for Theory Q3 😎

dn

🔥 Rolling forward!

⭐ Theory Q3
❓ Which module do we use for JSON in Python?
✅ Best Interview Answer

Python provides a built-in module called json for working with JSON data.
It supports converting Python objects to JSON (json.dump, json.dumps) and converting JSON back to Python objects (json.load, json.loads).

Reply done for Theory Q4 😎

dn

🔥 Great — keep the flow!

⭐ Theory Q4
❓ What is the difference between json.dump() and json.dumps()?
✅ Best Interview Answer

json.dump() converts a Python object to JSON and writes it directly to a file.
json.dumps() converts a Python object to a JSON string and returns it, without writing to a file.
The “s” stands for “string”.

Reply done for Theory Q5 😎

dn

🔥 Nice — next!

⭐ Theory Q5
❓ What is the difference between json.load() and json.loads()?
✅ Best Interview Answer

json.load() reads JSON data from a file and converts it into a Python object.
json.loads() converts a JSON string into a Python object.
The “s” again stands for “string”.

Reply done for the final theory Q6 😎

dn

💥 LAST THEORY — then we go 3 JSON coding questions just like pickling!

⭐ Theory Q6
❓ What types of Python objects can be converted to JSON?
✅ Best Interview Answer

Only JSON-serializable objects can be converted.
Python converts:

Python Type	JSON Equivalent
dict	object {}
list	array []
str	string
int/float	number
bool	true/false
None	null

Custom Python objects (like classes) cannot be directly converted unless we convert them manually (e.g., using __dict__).
"""




"""
Create a dictionary

Save it into data.json using json.dump()

Load it using json.load()

Print the data
"""

Info = {
    'Name' : 'Sheetal',
    'Id' : 11,
    'Age' : 22
}

# import json


# with open('data.json', 'w') as f:
#     json.dump(Info, f)

# with open('data.json', 'r+') as f:
#     obj = json.load(f)
#     print(obj)




"""
Create a list of 5 city names

Save it to cities.json

Load back and print each city in a loop
"""

import json

# city = ["Mumbai", "Pune", "Bangalore", "Hyderabad", "Chennai"]


# with open('city.json', 'w') as f:
#     json.dump(city, f)

# with open('city.json', 'r') as f:
#     obj = json.load(f)
#     print(obj)




"""
Create class Student with:

name

marks

Create 2 objects

Convert them to dicts using:

student.__dict__


Save list of dicts to students.json

Load and print each student like:
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Name is {self.name}\nMarks are: {self.marks}")


s1 =Student("sheetal", 95)
s2 =Student("sakshi", 95)
    
student = [s1.__dict__, s2.__dict__]


with open('student.json', 'w') as f :
    json.dump(student, f)

with open('student.json', 'r') as f:
    obj = json.load(f)
    print(obj)