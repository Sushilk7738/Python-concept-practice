# creating students record using Oops


class Student:
    def __init__(self, name, roll, percentage, team):
        self.name = name
        self.roll = roll
        self.percentage = percentage
        self.team = team

    def student_details(self):
        print(f"Student name: {self.name} | Student roll: {self.roll} | Percentage: {self.percentage} % | Team: {self.team}")

team1 = 'S'


s1 = Student("Sushil", 11, 83.20, team1)
# s2 = Student("Sheetal", 10, 79)
# print(s1.name,"weds",s2.name)

# s1.student_details()


# modify the object's properties
# print(s2.__dict__)
# s2.percentage = 90
# del s2.percentage
# print(s2.__dict__)








#abstraction:- hiding unnessary details from the user through class and method

class Student:
    def __init__(self, name, roll, percentage):
        self.name = name
        self.roll = roll
        self.percentage = percentage

    def details(self):
        print(f"Name: {self.name} | Roll: {self.roll} | Percentage: {self.percentage + 2}")


s1 = Student("Sushil", 10, 94)
s2 = Student("Sheetal", 12, 97)

# s1.details()


# Encapsulation:- Restrict access to certain attributes or methods to protect data and enforce controlled access

class Company:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.__salary = salary

    def details(self):
        print(f"Name: {self.name} | Role: {self.role}")

    def salary(self):
        return self.__salary

e1 = Company("Sushil", "Python Developer", 82000)

# e1.details()
# print(e1.salary())
# print(e1.__salary)






# Inheritance: it allows one class to inherit properties and methods to other class and supports reusability.


class Company:
    def __init__(self, c_name, industry, location):
        self.c_name = c_name
        self.industry = industry
        self.location = location

    def details(self):
        print(f"Company Name: {self.c_name} | Industry: {self.industry} | Location: {self.location}")

class Employee(Company):
    def __init__(self, name, c_name, industry, salary, role, location):
        super().__init__(c_name, industry, location)
        self.name = name
        self.salary = salary
        self.role = role

    def details(self):
        super().details()
        print(f"Name: {self.name} | Role: {self.role} | Company: {self.c_name} | Location: {self.location}")


c1 = Company("Infotech", "IT", "MUMBAI")
e1 = Employee("Sushil", "Infotech", "IT", 1580000, "Software Developer", "Mumbai")
e1.details()