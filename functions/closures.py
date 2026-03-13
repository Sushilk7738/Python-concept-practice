# function as a variable

# def greet():
#     print("Hey folks Good evening!")

# g = greet
# g()


# nested functions

# def outer():
#     def inner():
#         print('inner function')
#     inner()

# outer()


# def outer():
#     x = 20
#     def inner():
#         nonlocal x 
#         x += 4
#         print(x)
#     return inner

# x = outer()
# x()




# def counter():
#     count = 0
    
#     def increment():
#         nonlocal count
#         count +=1
#         return count
#     return increment

# c = counter()
# print(c())
# print(c())
# print(c())



def power(n):
    def calc(x):
        return x ** n
    return calc

square = power(2)
cube = power(3)

print(square(3))
print(cube(4))