# Python generators are simple ways to creating iterators

# creating a generator function:-

# def my_gen():
#     yield 'Sushil kamble is Python Developer'
#     yield 'He is very smart and interllectual'

# g = my_gen()

# print(next(g))
# print("----------------")
# for ele in g:
#     print(ele)

# print(next(g))






# import time 

# def countdown(num):
#     print("Countdown starting")
#     print("="*25)

#     while num > 0 :
#         yield num
#         time.sleep(1)
#         num = num -1

# num = int(input("Enter number: "))        
# g = countdown(num)

# for count in g:
#     print(count)






# shorthand way to create generators:-

# write a python program to finding squares of first n numbers 

import sys

# n = int(input('Enter number: '))
# squares = [i**2 for i in range(1, n+1)]   #list comprehension
# print(type(squares))
# print(sys.getsizeof(squares))

# squares = (i**2 for i in range(1, n+1))    #generator
# print(type(squares))
# print(sys.getsizeof(squares))

# print(next(squares))

#* when you write tuple comrehension code that is generator the concept of tuple comrehension doesnt exist in python



# fibonacci series using generators:- 

# def fibo():
#     first, second = 0, 1
#     while True:
#         yield first
#         first, second = second, first + second

# g = fibo()
# n = int(input('Enter a number: '))
# for i in g:
#     if i >= n:
#         break
#     print(i)



"""
Suppose you have a list of numbers, and you want to filter out even numbers, square the filtered even numbers,
and then sum them up.
"""


# def filter_even(seq):
#     for i in seq:
#         if i%2 ==0 :
#             yield i 

# def find_square(seq):
#     for num in seq:
#         yield num * num
        
# def addition_of_square(seq):
#     total_sum = 0
#     for i in seq:
#         total_sum = total_sum + i
#     yield total_sum
    
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total_sum = 0
# g = filter_even(numbers)

# g1 = find_square(g)

# g2 = addition_of_square(g1)

# print(next(g2))