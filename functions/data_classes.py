# traditional way to create class:-

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Sushil", 98)

# print(s1)






from dataclasses import dataclass, field

# @dataclass
# class Student:
#     name: str
#     marks : int

# s1 = Student("Sushil", 98)
# s2 = Student("Sheeta", 88)
# print(s1==s2)



# @dataclass
# class User:
#     name : str
#     age : int = 18
#     active : bool = True

#     def __post_init__(self):
#         print("User created")

# t = User("Sushil",)
# print(t)





# field in dataclass:-

# @dataclass
# class Product:
#     name: str
#     tags: list = field(default_factory=list)

# p = Product("Asus Laptop", ['i11', '16 GB RAM', '564GB SSD'])
# p1 = Product("Vivo Laptop", ['i7', '8 GB RAM', '564GB SSD'])
# print(p)
# print(p1)



# frozenset in dataclass:-

# @dataclass(frozen= True)
# class Point:
#     x : int
#     y : int

# p = Point(2, 9)
# p.y = 10
# print(p)



