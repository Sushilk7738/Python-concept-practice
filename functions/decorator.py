# function as argument:-

# def shout(func):
#     func()

# def sayMyName():
#     print("Daddy's home..")
# shout(sayMyName)


# def myDecorator(func):
#     def wrapper(a, b):
#         print('Function started')
#         func(a, b)
#         print('Function ended')
#     return wrapper


# @myDecorator
# def sub(a, b):
#     print(a - b)

# # sub = myDecorator(sub)
# sub(11, 5)





# def myDecorator(func):
#     def wrapper(*args, **kwargs):
#         print("function started")
#         func(*args, **kwargs)
#         print("function ended")
#     return wrapper

# @myDecorator
# def show(name , age):
#     info = {
#         'name' : name,
#         'age' : age
#     }
#     print(info)

# show("Sushil", 24)

# @myDecorator
# def notify(alert = "be safe"):
#     alert = "Before going to bed put mobile outside of your room."
#     print(alert)
# notify()





# we gonna use timer for programme time taken 

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time taken by programme: ", end - start)
    return wrapper

@timer
def slow():
    for i in range(1000000000):
        pass

slow()
    
