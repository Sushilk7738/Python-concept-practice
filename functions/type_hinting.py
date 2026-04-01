""" 
*Type hinting means providing hints about the datatypes in your code specifying:
1. Input parameter types
2. Funtion return types
"""

# without type hint:

# def add(a, b):
#     return a + b


# without type hint:
# def add(a:int, b: int)-> int:
#     return a + b



# def login(username: str, password:int) -> bool:
#     if username == "admin" and password == 1234:
#         return True
#     return False

# print(login("admin",1234))




"""
*NewType in typehinting:-
NewType creates distinct types based on existing one Providing logical separation even if the underlying type is the same
"""


# from typing import NewType

# UserID = NewType("UserID", int)
# ProductID = NewType("ProductID", int)

# def get_user(userid: UserID):
#     print(type(userid))
#     return userid

# get_user(1236)






# dataclasses with type hinting:

# from dataclasses import dataclass
# from typing import NewType

# UserID = NewType("UserID", int)
# userName = NewType("userName", str)

# @dataclass
# class User:
#     id : UserID
#     name: userName

# s = User(11, "Sushil")

# print(s)




from typing import Dict

student : Dict[str, int] = {"name":"sush", "age": 22}

print(student)