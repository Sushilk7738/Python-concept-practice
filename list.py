
#*how to flattend nested list which consist only sublist:
# nums = [[3 ,3, 4, 5, 6, 7, 9], [3 ,3, 4, 5, 6, 7, 9]]
# flat = []
# for i in nums:
#     for j in i:
#         flat.append(j)
# print(flat)





"""
*List Comprehension:- 
before that we should know about what  is comprehension?
=>It is way of writing compact code in python
There are three types of comprehension:-
1.list comprehension 2.set comprehension 3. Dictionery comprehension

List comprehension is a way to create list in consise way 

*syntax 01 (normal) :- [expression for variable in iterable]

*syntax 02 (if condn) :- [expression for variable in iterable if cond]

*syntax 03 (Nested if's) :- [expression for variable in iterable if cond1 if cond2]

*syntax 04 (if else) :- 
*[expression if cond else expression for variable in iterable]

"""


#*syntax 01 expression ex [expression for variable in iterable]:-

nums = [3 ,3, 4, 5, 6, 7, 9]

# sq = [i**2 for i in nums]
# print(sq)



# *syntax 02 (if condn) :- [expression for variable in iterable if cond]
# find the square of even nums:-
# nums = [3 ,3, 4, 5, 6, 7, 9]

# print([i*i for i in nums if i%2==0])


#*syntax 03 (Nested if's) :- [expression for variable in iterable if cond1 if cond2]
# find the square of numbers which divisble by 2, 3:-

# nums = [3 ,3, 4, 5, 6, 7, 9]

# print([i*i for i in nums if i%2 ==0 if i%3==0])



# *syntax 04 (if else) :- 
# *[expression if cond else expression for variable in iterable]
# in below list if number is even then square or if odd then cube.
# nums = [3 ,3, 4, 5, 6, 7, 9]
# print([i*i if i%2==0 else i**3 for i in nums])



# *syntax 05 (nested for loops) [expression for variable in iterable for char in iterable]:- 
# lst = [[3 ,3, 4, 5, 6, 7, 9], [3 ,3, 4, 5, 6, 7, 9]]
# print([j for i in lst for j in i])


# practice:-

# *Create a list of squares of numbers from 1 to 10 using list comprehension.

# print([i * i for i in range(1, 11) ])



# *From this list, create a new list containing only even numbers.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([i for i in nums if i%2==0])


#* Convert this list of strings into integers using list comprehension:

nums = ["1", "2", "3", "4", "5"]

# print([int(i) for i in nums if isinstance(i, str)])


#* From the list below, create a new list containing length of each word.
# words = ["python", "java", "c", "golang"]

# print([len(i) for i in words ])

"""
From the list below, create a new list where:

If the number is even, keep it

If the number is odd, replace it with 0
"""
nums = [1, 2, 3, 4, 5, 6]

# print([0 if i%2!=0 else i for i in nums])




# From the list below, create a list of squares of even numbers only.
# nums = [1, 2, 3, 4, 5, 6]

# print([i for i in nums if i%2==0])



#* From the list below, create a new list that contains squares of only odd numbers.

# nums = [1, 2, 3, 4, 5, 6, 7]
# print([i*i for i in nums if i%2!=0])
