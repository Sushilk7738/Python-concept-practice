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





"""
Write a Python script that:

1️⃣ Defines a Student class with

name

roll

marks

2️⃣ Supports three operations:

Add student (create & store object)

View all students (read & print objects)

Exit (stop program)

3️⃣ Use pickling with persistence

On each add, append the object to students.pkl

When viewing, unpickle all objects and print them"""

# import pickle
# import os

# class Student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks
    
#     def display(self):
#         print(f"Name is: {self.name}\nRoll is: {self.roll}\nMarks are:{self.marks}")

    
# FILE = 'student.pkl'

# def add_student():
#     name = input('Enter your name: ')
#     roll = int(input("Enter roll: "))
#     marks = float(input("Enter marks: "))

#     student = Student(name, roll, marks)

#     with open(FILE, 'ab') as f:
#         pickle.dump(student, f)
#     print('Student added successfully!\n')


# def view_student():
#     if not os.path.exists(FILE):
#         print("No students found!\n")
#         return
    
#     with open(FILE, 'rb') as f:
#         print("========= Student list =========")
#         while True:
#             try:
#                 student = pickle.load(f)
#                 student.display()
#             except EOFError:
#                 break
#             print("="*50,"\n")



# while True:
#     print('1. Add student')
#     print('2. View student')
#     print('3. Exit ')

#     choice = input("Enter choice: ")

#     if choice == "1":
#         add_student()
    
#     elif choice == '2':
#         view_student()
    
#     elif choice == '3':
#         break
    
#     else:
#         print("Invalid choice\n")






"""
Create a dictionary with 3 fields
Save it to data.pkl using pickling
Load it back and print it."""

# import pickle

# userData = {
#     'Name' :"Sushil",
#     'Id' :11,
#     'Designation' : 'Software Engineer'
# }

# with open('userData.xyz', 'wb') as f:
#     pickle.dump(userData, f)

# with open('userData.xyz', 'rb') as f:
#     while True:
#         try:
#             obj = pickle.load(f)
#             print(obj)
            
#         except EOFError:
#             break
    

# import pickle
    
# nums = [1, 2, 3, 4, 5]

# with open('nums.ninja', 'wb') as f:
#     pickle.dump(nums, f)

# with open('nums.ninja', 'rb') as f:
#     obj = pickle.load(f)
    
# for item in obj:
#     print(item, end = ' ')


# import pickle

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(f"Name is: {self.name}\nAge is: {self.age}\n{'='*25}")



# p1 = Person("Nobita", 12)
# p2 = Person("Sitzuka", 12)

# persons_list = [p1, p2]

# with open('person.dor', 'wb') as f:
#     pickle.dump(persons_list, f)

# with open('person.dor', 'rb') as f:
#     obj = pickle.load(f)
    
#     for i in obj:
#         i.display()




