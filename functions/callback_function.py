# callback function:-



# def greet():
#     print("""Hey champ dont worry You are not late god is seeing ur effort 
#         and will bless you when your time come just keep going...""")

# def execute(call):
#     call()

# execute(greet)



# def calc(a, b, callback):
#     result = a + b
#     callback(result)

# def show_result(res):
#     print("Result: ", res)

# calc(5, 6, show_result)



students = [
    {"name": "Sushil", "marks": 98},
    {"name": "Sheetal", "marks": 89},
    {"name": "Nikita", "marks": 78},
]

# def get_marks(student):
#     return student["marks"]

# students.sort(key=get_marks)

# print(students)


# using lambda:-
students.sort(key=lambda x : x["marks"])
print(students)