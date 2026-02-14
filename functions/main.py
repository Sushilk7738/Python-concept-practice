# def print_line():
#     print("-----------------------")

# print_line()

"""
# *Function Definition vs Function Calling

Function definition registers the function object in memory

Function call:

Transfers control to the function

Executes its body

Returns control back to caller
"""



# def demo():
#     print("Inside function")

# print("Start")
# demo
# print("End")





"""
The parameters are the values which defined in function definition i.e placeholders 
and arguments are the actual values which are given in function call and this both 
can be matched when the function invokes.
"""
# def multiply(x, y):   # parameters → x, y
#     print(x * y)

# multiply(3, 4)        # arguments → 3, 4



"""
positional arguments:-

Positional Arguments are assigned to parameters based on their position

This is the default argument-passing mechanism in Python

Incorrect order leads to incorrect results or logical bugs
"""



# def calc(a, b):
#     s = a + b
#     m = a * b
#     d = a / b

#     return f"addition: {s} , multiplication: {m}, division: {d}"

# print(calc(6, 5))


"""
#* What are positional arguments in Python?

Positional arguments are arguments that are passed to a function based on their position 
in the function call. The order of arguments must match the order of parameters defined 
in the function.
"""

"""
#* What are positional arguments in Python?
Keyword arguments are arguments passed using parameter names during the function call. 
They are used to improve readability, avoid errors caused by incorrect ordering, 
and make function calls self-documenting.
"""

"""
#* Can positional arguments come after keyword arguments?

No. Positional arguments must always come before keyword arguments in a function call.
Otherwise, Python raises a SyntaxError.

"""


# def calculate_bill(price, tax=5, discount = 0):
#     final_amount = price + (price * tax / 100) - discount
#     print(final_amount)

    
# calculate_bill(100)
# calculate_bill(100, 10)
# calculate_bill(100, 10, 20)



# def create_profile(name, age, city):
#     print(f"Name: {name}\nAge: {age}\nCity: {city}")

# create_profile(name="Kate", age=25, city= 'Mumbai')




# Write a function send_email(to, subject="No Subject", priority="Normal") that prints:

# def send_email(to, subject = "No subject", priority = "Normal"):
#     print(f"{'='*25}\nTo : {to}\nSubject: {subject}\nPriority: {priority}\n{'='*25}")

# send_email("Infosys", subject="Python Fullstack Developer Role")


"""
* variable length argument:-

*args allows a function to accept a variable number of positional arguments.
All extra positional arguments are packed into a tuple inside the function.
The name args is a convention; the * is what enables variable length.

*args is preferred because it makes functions flexible and reusable when the number of inputs is unknown.
"""


"""
Is args a keyword in Python? Explain briefly.

✅ INTERVIEW ANSWER (2–3 lines)

No, args is not a keyword in Python.
It is just a naming convention; the * operator is what allows variable-length positional arguments.
You can name it anything, but args is commonly used for readability.

"""

"""
What is the data type of args inside a function and why?

✅ INTERVIEW ANSWER (2–3 lines)

Inside the function, args is a tuple.
This is because tuples are immutable, which makes handling variable positional arguments safer and more efficient.

"""


# def max_value(*args):
#     if not args:
#         return None
#     else:
#         return max(args)
        
# print(max_value(3, 7, 2, 9))
# print(max_value(10))
# print(max_value())


"""
Write a function average(*args) that:

Accepts any number of integers

Returns the average

If no arguments are passed, return 0"""

# def average(*args):
#     if not args:
#         return 0
#     else:
#         return sum(args)/len(args)

# print(average(10, 20, 30))
# print(average(5))
# print(average())


"""
Write a function print_items(title, *items) that:

title is a normal positional argument

*items can take any number of values

The function should print the title first, then each item on a new line
"""


# def print_items(title, *items):
#     print("============", title, "============\n")
#     for i in items:
#         print(f"- {i}\n")

# print_items("Shopping List", "Milk", "Bread", "Eggs")




"""
What is **kwargs in Python?

✅ Interview Answer (2–3 lines)

**kwargs allows a function to accept a variable number of keyword arguments.
All keyword arguments are collected into a dictionary inside the function.
The name kwargs is a convention; the ** enables variable-length keywords.

"""



"""
What is the data type of kwargs inside a function and why?

✅ Interview Answer (2–3 lines)

Inside the function, kwargs is a dictionary.
This is because keyword arguments are passed as key–value pairs, 
where keys are parameter names and values are the corresponding arguments."""



"""
is kwargs a keyword in Python? Explain briefly.

✅ Interview Answer (2–3 lines)

No, kwargs is not a keyword in Python.
It is just a naming convention; the ** operator is what allows a function to accept variable-length keyword arguments.

"""



"""
Where must **kwargs be placed in a function’s parameter list?

✅ Interview Answer (2–3 lines)

**kwargs must be placed after all other parameters, including normal parameters and *args.
It should always be the last parameter in the function definition.
"""

"""
Can a function have both *args and **kwargs? If yes, in what order?

✅ Interview Answer (2–3 lines)

Yes, a function can have both.
The correct order is: normal parameters → *args → **kwargs.
This ensures positional arguments are collected first, then keyword arguments.
"""



"""
Write a function print_details(**kwargs) that:

Accepts any number of keyword arguments

Prints each key and value in this format:
"""

# def print_details(**kwargs):
#     for i, j in kwargs.items():
#         print(f"{i} : {j}")

# print_details(name = "Amit", age = 25, city = "Mumbai")




"""
Write a function get_value(key, **kwargs) that:

Returns the value for key if it exists in kwargs

Otherwise returns "Not Found
"""

# def get_value(key, **kwargs):
#     if key in kwargs:
#         return kwargs[key]

#     else :
#         return "Not found"

# print(get_value('age', name = "Amit", age= 25))
# print(get_value('salary', name = "Amit", age= 25))




"""
Write a function merge_dicts(**kwargs) that:

Accepts any number of keyword arguments

Returns them as a dictionary
"""


# def merge_dicts(**kwargs):
#     return kwargs

# print(merge_dicts(a=1, b=2, c=3))




"""
Write a function update_profile(profile, **kwargs) that:

profile is a dictionary

Updates profile using key–value pairs from kwargs

Returns the updated dictionary
"""

# def update_profile(profile, **kwargs):
#     profile.update(kwargs)
#     return profile

# profile = {'name': 'Amit', 'age': 25}
# print(update_profile(profile, city= 'Mumbai', age=26))



"""
Write a function filter_even(**kwargs) that:

Accepts any number of keyword arguments where values are integers

Returns a dictionary containing only those key–value pairs where the value is even
"""

def filter_even(**kwargs):
    updated = {}
    for i,j in kwargs.items():
        if j % 2 == 0:
            updated[i] = j
    return updated

print(filter_even(a=10, b=15, c=20, d=7))
