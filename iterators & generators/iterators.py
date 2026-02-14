"""
#* Iteration:- process of taking each item of collection one after another.
ex:- Whenever you use a loop for visiting every item of sequence.
"""

"""
*Iterator :- It is an object that allows programmers to traverse through a sequence of data
without storing data in the memory
"""

"""
Iterable :- It is an collection of data on which iteration process performs.
"""

# how to create iterator?

L = [10,20,30,40]  #iterable
iter_obj = iter(L)

# print(iter_obj)
# print(type(iter_obj))

# print(next(iter_obj))
# print("*"*25)
# print(next(iter_obj))

# for ele in iter_obj:
#     print(ele)

#* Iter object remembers the previous state of iterable items.



# How to check whether an object is iterable or not ?
# How to check an object is iterable or iterator ?

# L = [10,20,30,40]  #iterable but not iterator
# print('L', dir(L))

# iter_obj = iter(L)  #iterator

# print('iter_obj', dir(iter_obj))




#* Every iterator is iterable. You can run loop on every iterator. 

# to find any object is iterable or iterator you can use magic method:- 

#* if __iter__ is only present in object then it is "Iterable".
#* if __iter__ , __next__  present in object then it is "Iterator".


# L = [11, 22, 33, 44]

# #using magic method
# iter_obj = L.__iter__()   #iterator
# print(type(iter_obj))

# print(iter_obj.__next__())




# when you create an iterator of iterator then it returns itself

# L = [11, 22, 33, 44]

# iter_obj = iter(L)
# print('id of iter_obj', id(iter_obj))

# iter_obj1 = iter(iter_obj)
# print('id of iter_obj1', id(iter_obj1))

# print(iter_obj1.__next__()) 




#* program for checking iterator or iterable

# object1 = iter(eval(input('Enter object: ')))
# object_dir = dir(object1)

# if '__iter__' in object_dir and '__next__' in object_dir:
#     print("It is an iterator")

# elif '__iter__' in object_dir:
#     print("It is an iterable")

# else:
#     print('Not supported')




#* making our own for loop

# L = [10, 20, 30, 40]

# def my_loop(iterable):
#     iterator = iter(iterable)
#     try: 
#         while True:
#             print(next(iterator))
#     except StopIteration:
#         pass

# my_loop(L)




# what is biggest advantage of iterator? 
# It saves memory.

# i want to find square of first 10 numbers
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 1st approch 

import sys

# for ele in L:
    # print(ele **2)
# print('L', sys.getsizeof(L))


# 2nd approch:-
a = range(1, 11111111111111111111111111111111)
# for ele in a:
#     print(ele**2)
# print('a',sys.getsizeof(a))



"""
Lazy Evaluation: Iterators allow for lazy evaluation of elements, which means elements are generated on-the-fly
as they are requested saving memory and improving performance when dealing with large datasets.

"""

"""
Types of iterator:- 
- built in iterators (runs iternally)
ex. iterator of range() function

- Custom iterators
"""



# class Power_of_two:
#     def __init__(self, max_value):
#         self.limit = max_value
#         self.current = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current <= self.limit:
#             result = self.current
#             self.current = self.current *2
#             return result
        
#         else:
#             raise StopIteration

# n = int(input('Enter the limit: '))
# iter_obj = Power_of_two(n)

# # print(next(iter_obj))
# for el in iter_obj:
#     print(el)





# own range() function

class my_range:
    def __init__(self, start=0, stop=None, step=1):
        if stop is None:
            raise TypeError
        
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return my_range_iterator(self)

class my_range_iterator:
    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj

    def __iter__(self):
        return self
    
    def  __next__(self):
        if self.iterable_obj.start < self.iterable_obj.stop:
            result = self.iterable_obj.start
            self.iterable_obj.start = self.iterable_obj.start + self.iterable_obj.step
            return result

        else:
            raise StopIteration
        
a = my_range(2, 10, 3)
iter_obj = iter(a)

# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

for ele in my_range(2, 20, 3):
    print(ele)  
    
print()

for ele in range(2, 20, 3):
    print(ele)  