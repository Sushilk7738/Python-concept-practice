"""Coding Question 1:

Task: Write a simple piece of code where you pickle a dictionary object to a file named data.pkl and then unpickle it back into a Python object."""



# import pickle

# info_dict = {'Name': 'Sushil', 'Id': 11}

# f = open('data.pkl', 'wb')
# byte_data = pickle.dump(info_dict, f)
# f.close()


# with open('data.pkl', 'rb') as f:
#     obj = pickle.load(f)
#     print(obj)



"""
Create a list containing three dictionaries
Example fields:

"name"

"age"

"city"
2️⃣ Pickle the list to a file named users.pkl
3️⃣ Unpickle it and print each user one-by-one
"""

# import pickle

# users_list = [{'name': 'sushil', 'age': 22, 'city' : 'Mumbai'},
#         {'name': 'sheetal', 'age': 22, 'city' : 'Mumbai'},
#         {'name': 'akansha', 'age': 19, 'city' : 'Bangalore'},
#     ]

# #pickling

# f = open('users.pkl', 'wb')
# pickle.dump(users_list, f)
# f.close()

# # unpickling

# with open('users.pkl', 'rb') as f:
#     data = pickle.load(f)
#     print(data)





"""
Create a class Student with attributes

name

roll

marks

2️⃣ Create three objects of the class and store them in a list

3️⃣ Pickle this list to a file students.pkl

4️⃣ Unpickle it, and print each student's data in this format:

# """
# import pickle

# class Student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks
        
#     def display(self):
#         print(f"Name is: {self.name}\nRoll is: '{self.roll}'\nMarks are: {self.marks}")

# s1 = Student("sushil", 11, 99)
# s2 = Student("sheetal", 12, 97)
# s3 = Student("akansha", 13, 91)

# students_list = [s1, s2, s3]

# #pickling
# with open('students.pkl', 'wb') as f:
#     pickle.dump(students_list, f)

# #unpickling
# with open('students.pkl', 'rb') as f:
#     obj = pickle.load(f)
   
# for students in obj:
#     students.display()





"""
1️⃣ Create a class Employee with

name

salary

2️⃣ Create two Employee objects

3️⃣ Pickle the first object into a file named employees.pkl

4️⃣ Append the second object to the same file
⚠️ Without overwriting the first one

5️⃣ Unpickle the file and print both employees

"""

# import pickle

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     def display(self):
#         print(f"Name is {self.name}\nSalary is: {self.salary}")

# e1 = Employee("Sushil", "1250000")
# e2 = Employee("Sheetal", '100000')

# with open("employees.pkl", 'wb') as f:
#     pickle.dump(e1, f)

# with open('employees.pkl', 'ab') as f:
#     pickle.dump(e2, f)

# employees = []

# with open('employees.pkl', 'rb') as f:
#     while True:
#         try:
#             employees.append(pickle.load(f))
#         except EOFError:
#             break


# for emp in employees:
#     emp.display()