import json

data = {
    "name": "Sushil",
    "age" : 24,
    "course": "Full Stack Python Developer"
}

# create json string:-
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)


# create json string to python object:-

# with open("data.json", 'r') as f:
#     loaded_data = json.load(f)
#     # print(type(loaded_data)) 
#     # print(loaded_data) # python obj
#     c = json.dumps(loaded_data)
#     print(c)   # json string



data = {"student": {
    "name" : "Sushil",
    "marks" :[80, 90, 98],
    "teacher":{
        "name" : "Shweta yadav",
        "subjects": ["Maths", "English", "History"],
    }
}}

# print(data["student"]["name"])
# print(data["student"]["marks"][2])

# print(json.dumps(data, indent=4))


# try:
#     bad_data= "{name: sam}"
#     json.loads(bad_data)
# except json.JSONDecodeError:
#     print("Invalid format")






# from datetime import datetime

# time = json.dumps(datetime.now(), default=str)
# time = json.dumps(datetime.now().isoformat())
# print(time)



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Sushil", 98)

# print(json.dumps(s1.__dict__))






# with dataclasses integration:-
import dataclasses
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int

s1 = Student("Sushil",97)
print(dataclasses.asdict(s1))