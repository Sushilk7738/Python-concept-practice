""" #*What is a dictionary in Python? How is it different from a list or tuple?
A dictionary in Python is a built-in data type used to store data in key–value pairs.
where each key is unique and maps to a value,
Data is accessed using keys not index numbers.
"""


"""#*Are dictionaries mutable in Python? What operations can you perform because of this?
Yes, dictionaries in Python are mutable, which means you can change their contents after creation.

#*Keys must be immutable (string, number, tuple)

#*Values can be any data type

#*Changes happen in the same dictionary object (no new object is created)

Python dictionaries are mutable. This means we can add, update, or remove key–value pairs
after creation. We can modify values directly, add new keys, or delete existing ones 
the del keyword. The keys must be unique and immutable (like strings or tuples), 
while the values can be any data type. Importantly, all changes happen in the
same dictionary object—no new object is created.
"""
#*Add new key–value pairs
student = {"name" : "Sushil", "age" : 23}

# student["city"] = "Pune"

# print(student)

#*Update existing value 
# student["age"] = 21
# print(student)


# *Delete key-value pairs
# del student["age"]
# print(student)






"""
# What are valid and invalid data types for dictionary keys in Python? Why does Python enforce this rule?

“Dictionary keys must be immutable and hashable because Python uses hashing for fast key lookup.”

valid key data types:-

"string"      # ✅
123           # ✅
3.14          # ✅
(True, False) # ✅ tuple (only if it contains immutable elements)

invalid data types:- list, dict, set

#*Python uses a hashing mechanism internally for dictionaries:

#*Keys are stored based on their hash value

#* If a key could change (mutable), its hash could change
#* That would break fast lookup and data integrity.

In Python, dictionary keys must be immutable and hashable because 
Python uses hashing for fast key lookups. 
Immutable types—like strings, integers, or tuples (if the tuple is immutable)
—ensure that the key’s hash never changes. 
Using mutable keys would break the hashing system and 
compromise both speed and data integrity. That’s why keys must be immutable.
"""


# practice starts:-

info = {"name" : "Sush", "age" : 21, "city" : "pune"}
# print(info)


# print(info["name"])

# info['age'] = 23
# print(info)

# info['role'] = "Python Developer"
# del info["city"]
# print(info)

# print(info.get("age"))
# print(info.get("salary"))


# for key, value in info.items():
#     print(f"{key}: {value}", end=' ')


#only keys

# for key in info:
#     print(key)

#only values
# for values in info.values():
#     print(values)

#key value 
# for k, v in info.items():
#     print(k ,":", v)



# Create a dictionary that stores the frequency of each number.
nums = [1, 2, 2, 3, 1, 4, 2]

dict1 = {}

# for i in nums :
#     if i not in dict1:
#         dict1[i] = 1

#     else:
#         dict1[i] +=1

# print(dict1)

# for i in nums :
#     if i not in dict1:
#         dict1[i] = 1
        
#     else :
#         dict1[i]= dict1.get(i, 0) + 1
# print(dict1)




# marks = {
#     "python": 85,
#     "java": 78,
#     "django": 90,
#     "sql": 72
# }

# max_marks = 0
# top_sub = ""

# for sub, mark in marks.items():
#     if mark > max_marks:
#         max_marks = mark
#         top_sub = sub

# print(f"{top_sub} : {max_marks}")



"""
Create a new dictionary where:

values become keys

keys become values
"""
# data = {"a": 1, "b": 2, "c": 3}

# dict1 = {}

# for i , j in data.items():
#     dict1[j] = i

# print(dict1)




# Create a dictionary that stores frequency of each character.

# text = "python"

# dict1 = {}

# for i in text:
#     if i not in dict1:
#         dict1[i] = dict1.get(i, 0) + 1

# print(dict1)



# Remove all keys whose value is less than 60.
# scores = {"a": 50, "b": 80, "c": 30, "d": 90}
# updated = {}

# for i, j in scores.items():
#     if j > 60:
#         updated[i] = j

# print(updated)




# Merge both dictionaries into one new dictionary, without using: update() and | operator

# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}

# d3 = {}

# for i , j in d1.items():
#     d3[i] = j

# for k, v in d2.items():
#     d3[k] = v

# print(d3)




# Find the student name who has the highest total marks


# students = {
#     "sush": {"python": 80, "django": 85},
#     "rahul": {"python": 70, "django": 60},
#     "amit": {"python": 90, "django": 95}
# }

# highest_marks = 0
# student = ""

# for name, subjects in students.items():
#     total = 0
#     for marks in subjects.values():
#         total += marks
#     print(total)

#     if total > highest_marks:
#         highest_marks =total
#         student = name

# print(f'Highest marks {highest_marks} scored by {student}')




# Increase marks by +5 only for subjects whose marks are less than 60.

# marks = {
#     "python": 45,
#     "java": 65,
#     "django": 55,
#     "sql": 70
# }


# for i, j in marks.items():
#     if j < 60 :
#         marks[i] += 5

# print(marks)


# Create a list of all keys whose value is 50.

scores = {
    "a": 10,
    "b": 50,
    "c": 30,
    "d": 50,
    "e": 20
}

# updated = []


# for i, j in scores.items():
#     if j == 50:
#         updated.append(i)

# print(updated)





data = {"name": "Sush", "age": 23, "role": "Python Developer"}


# Check whether the key "email" exists in the dictionary and print True or False.

# print('email' in data)


# Check whether the value "Sush" exists and print True or False.
# data = {"name": "Sush", "age": 23, "role": "Python Developer"}
# print('Sush' in data.values())




# Print the number of keys in the dictionary.
# data = {"a": 1, "b": 2, "c": 3, "d": 4}

# print(len(data.keys()))


# Print the sum of all values in the dictionary.
# data = {"a": 10, "b": 20, "c": 30}

# print(sum(data.values()))


# Create a dictionary by pairing elements from both lists.
# keys = ["a", "b", "c"]
# values = [1, 2, 3]

# dict1 = {}

# for i in range(len(keys)):
#     dict1[keys[i]] = values[i]

# print(dict1)



# Create a new dictionary with values as keys and keys as values.

# data = {"x": 1, "y": 2, "z": 3}

# data1 = {}

# for i, j in data.items():
#     if j not in data1:
#         data1[j] = i

# print(data1)