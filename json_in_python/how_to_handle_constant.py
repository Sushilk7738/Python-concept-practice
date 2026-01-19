"""
what is constants ?
Name/variables whose value wont change after defined.

for ex:- pi = 3.14159

You cannot create constant or python has any facilites to create constants like other languages
* There is no direct keyword or mechanism to create constant in Python.

But there are some ways so that we consider as constant in python:-
*1. Using uppercase convention (it is changeble)
*2. Using module level variable
*3. Using enum module
*4. Use private variables

"""

# 1. using uppercase:- 

# PI = 3.14159

# 2. Using module level variable
# import constants
# print(constants.PI) 


# # 3. using enum module:-
# from enum import Enum

# class Constants(Enum):
#     PI = 3.14159
    
# # Constants.PI = 11
# print(Constants.PI.value)


# 4. Use private variable:- 

class Constants:
    __PI = 3.14159

print(Constants.__PI)