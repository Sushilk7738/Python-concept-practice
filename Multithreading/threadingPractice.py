"""Write a Python program using multithreading where:

Two threads increment a shared variable count

Each thread increments it 100000 times

Use Lock to prevent race condition

Final output must be 200000"""

from threading import * 

# count = 0
# l = Lock()
# def display():
#     global count
#     for _ in range(100000):
#         with l:
#             count +=1
    

# t1 = Thread(target=display)
# t2 = Thread(target=display)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Final count: ", count)



# from threading import * 
# count = 0

# def display():
#     global count
#     for _ in range(500000):
#         count +=1


# t1 = Thread(target=display)
# t2 = Thread(target=display)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Count is: ", count)

# from threading import * 
# l = Lock()
# count = 0

# def display():
#     global count 
#     with l:
#         for _ in range(100000):
#             count +=1

# td = Thread(target=display)
# td1 = Thread(target=display)

# td.start()
# td1.start()

# td.join()
# td1.join()

# print("count is: ",  count)


# from threading import *
# l = RLock()

# def display():
#     with l:
#         for _ in range(10):
#             print('hello')
            
# h = Thread(target=display)
# h1 = Thread(target=display)

# h.start()
# h1.start()