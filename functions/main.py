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

# def filter_even(**kwargs):
#     updated = {}
#     for i,j in kwargs.items():
#         if j % 2 == 0:
#             updated[i] = j
#     return updated

# print(filter_even(a=10, b=15, c=20, d=7))


"""



# ==========================================================================================================================================

*Return Statement :- 


#* What is the return statement in Python and what does it do?

The return statement is used to send a value back to the caller and terminate the function execution.
Once return is executed, no further code inside the function runs.
If no value is specified, it returns None.

"""



"""
* What is the difference between return and print in a function?

✅ Interview Answer (2–3 lines)

print only displays output to the console, but does not send data back to the caller.
return sends the result back to the calling code and can be used for further computation.
print cannot be used in expressions, while return can."""




"""
* What does a function return if there is no return statement?

✅ Interview Answer (2–3 lines)

If a function does not have a return statement, it implicitly returns None.
Even if the function executes successfully, Python always returns None by default."""


"""
*Can a function return multiple values in Python? If yes, how?

✅ Interview Answer (2–3 lines)

Yes, a function can return multiple values by separating them with commas.
Python packs these values into a tuple and returns it.
Multiple values can be unpacked by the caller.

"""


# ==========================================================================================================================================


# def square(num):
#     return num * num

# print(square(-5))







"""
Write a function divide(a, b) that:

Returns the result of a / b

If b is 0, return the string "Cannot divide by zero"

Use early return"""



# def divide(a, b):
#     try:
#         return a / b

#     except :
#         return 'Cannot divide by zero'

# a = int(input('enter number: '))
# b = int(input('enter number: '))
# print(divide(a, b))




# def divide(a, b):
#     if b == 0 :
#         return 'Cannot divide by zero'

#     else:
#         return a / b

# a = int(input('enter number: '))
# b = int(input('enter number: '))
# print(divide(a, b))


"""
Write a function safe_index(lst, value) that:

Takes a list lst and a value value

Returns the index of the value if it exists in the list

Returns -1 if the value is not present

Must use early return

Must not raise an error in any case"""



# def safe_index(lst, value):
#     if value not in lst :
#         return -1
    
#     else:
#         return lst.index(value)
            
# list = [10, 20, 30, 40]        
# print(safe_index(list, 40))


"""
Write a function validate_user(username, password) that:

Returns "Invalid input" if either value is empty or None

Returns "Weak password" if password length is less than 6

Returns "Valid user" otherwise

Must use multiple early returns

No printing inside the function"""




# def validate_user(username, password):
#     if not username and not password:
#         return 'Invalid input'

#     elif len(password) < 6 :
#         return 'Weak password'

#     else :
#         return 'Valid user'



# username = input('Enter username: ')
# password = input('Enter password: ')

# print(validate_user(username, password))



# Write a function calculate_grade(marks) that:

# Returns "Invalid" if marks is None or outside 0–100

# Returns "Fail" if marks < 40

# Returns "Pass" if marks ≥ 40 and < 75

# Returns "Distinction" if marks ≥ 75

# Must use early returns

# No printing inside function


# # 
# def calculate_grade(marks):
#     if marks is None or marks < 0 or marks > 100:
#         return 'Invalid'
#     elif marks < 40:
#         return 'Fail'    

#     elif marks >=40 and marks < 75:
#         return 'Pass'

#     elif marks >=75 :
#         return 'Distinction'

#     else:
#         return




# marks = int(input('Enter marks: '))

# print(calculate_grade(marks))





# ================================================================================================================

#* Scope in function:-

"""
* What is variable scope in Python?


Variable scope defines the region of the program where a variable is accessible.
In Python, scope determines where a variable can be read or modified.
It helps avoid name conflicts and controls variable lifetime.

"""



"""
* What are the different types of variable scope in Python?

Python has four types of scope, commonly remembered as LEGB:
Local, Enclosing, Global, and Built-in.
Python looks for variables in this order when resolving names.

"""



"""
* What is a local variable in Python?

✅ Interview Answer (2–3 lines)

A local variable is a variable defined inside a function.
It is accessible only within that function and exists only during the function’s execution.
Local variables are destroyed once the function finishes.
"""



"""
* What is a global variable in Python?

A global variable is a variable defined outside all functions.
It can be accessed inside functions, but to modify it inside a function, the global keyword is required.
Without global, Python treats it as a local variable.
"""


"""
* What is the nonlocal keyword in Python and when is it used?

nonlocal is used to modify a variable from an enclosing (outer) function, not the global scope.
It allows inner functions to update variables defined in the nearest enclosing scope.
Without nonlocal, Python treats the variable as local to the inner function.

"""




# x = 100

# def test():
#     print(x)
#     x = 50

# test()




# count = 0

# def increment():
#     global count
#     count +=1
#     print(count)

# increment()
# increment()
# increment()




# def outer():
#     x = 10

#     def inner():
#         nonlocal x
#         x += 5
#     inner()
#     print(x)

# outer()




"""
Write a program that:

Has a global variable total = 100

Has a function add(value) that:

Does not use global

Returns total + value

Prints the returned value

Ensures the global total remains unchanged"""



# total = 100

# def add(value):
#     return total + value

# print(add(50))






"""Write a program that:

Has a global variable x = 5

Defines a function modify() that:

Creates a local variable also named x

Sets local x = 20

Prints local x

After calling modify(), print global x

"""


# x = 5

# def modify():
#     x = 20
#     print(x)

# modify()
# print(x)





"""
Write a program that counts how many times a function is called, using scope rules, with these constraints:

🔒 Constraints (important)

You are NOT allowed to use:

Classes

Global variables

You MUST use:

A function inside another function

nonlocal

The outer function should return the inner function

Each time the returned function is called, the count should increase"""




# def make_counter():
#     count = 0

#     def counter():
#         nonlocal count
#         count +=1
#         return count
#     return counter

# counter = make_counter()

# print(counter())
# print(counter())
# print(counter())



        
        
        
# Has a function create_multiplier(n)

# Inside it, define another function multiply(x)

# multiply(x) should return x * n

# create_multiplier should return the multiply function

# Use scope properly (no globals)


# def  create_multiplier(n):
    
#     def multiply(x):
#         return x * n
#     return multiply
    
# double = create_multiplier(5)
# print(double(5))



