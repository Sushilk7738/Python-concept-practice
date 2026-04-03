"""
While execution multiple threads performs operations on same variable of value
then results are unexpected
"""
# for ex:- Bus ticketing system

# from threading import Thread, current_thread

# class Bus:
#     def __init__(self, name, available_seats):
#         self.name = name
#         self.available_seats = available_seats
    
#     def reserve(self, seats_need):
#         print(f"Seats are available: {self.available_seats}")

#         if self.available_seats >= seats_need:
#             nm = current_thread().name
#             pass
#             print(f"{seats_need} are allocated to {nm}")
#             self.available_seats -= seats_need

#         else:
#             print("Sorry! seats are not available.")

# b1 = Bus('Ashoka', 2)

# t1 = Thread(target=b1.reserve, args=(2,), name="Sushil")
# t2 = Thread(target=b1.reserve, args=(1,), name="Sheetal")
# t1.start()
# t2.start()

"""
What is race condition:- 
It is bug generated when you do multi-processing. It occurs because two or more 
threads tries to update the same variable and results into unreliable output

"""

# to avoid race condition Lock in multithreading:-
"""
*Thread synchronization techinques:- 

Thread synchronization defined as mechanism which ensures two or more concurrent threads
do not execute simultaneously some particular program segment which known as critical 
section.

1. Using locks
2. Using R-locks
3. Using semaphores
"""


# 1. Locks in python:- 
# Threading module provides a lock class to deal with the race condition.

from threading import *
import time

# myLock = Lock()  #step-1

# def task(myLock, msg):
#     myLock.acquire(blocking = False)
#     for i in range(5):
#         print(msg)
#     time.sleep(3)
#     myLock.release()

# t1 = Thread(target=task, args=(myLock,"Sushil is best Software Engineer."))
# t2 = Thread(target=task, args=(myLock, "He is now so successful and earning in crores."))

# t1.start()
# t2.start()



# Now we use this locking in earlier example bus seating program.

# lock = Lock()

# class Bus:
#     def __init__(self, available_seats, name, l):
#         self.available_seats = available_seats
#         self.name = name
#         self.l = l

#     def reserve(self, need_of_seats):
#         self.l.acquire()
#         print(F"Available seats are {self.available_seats}")

#         if self.available_seats >= need_of_seats:
#             name = current_thread().name
#             print(f"{need_of_seats} are allocated to {name}")
#             self.available_seats -= need_of_seats
#         else:
#             print("Sorry.. seats are not available.")
#         self.l.release()
        
# b1 = Bus(2,"Ashoka travels", lock)

# t1 = Thread(target=b1.reserve, args=(2, ), name="Sushil")
# t2 = Thread(target=b1.reserve, args=(1, ), name="Sheetal")

# t1.start()
# t2.start()

"""
there is drawback using locks is that we gonna tried to multiple locks and release in program
program crashes and results into error.

So overcome from this problem R-lock introduced.

R-Lock is modified mechanism of Locks.
"""



# lock = RLock()

# class Bus:
#     def __init__(self, available_seats, name, l):
#         self.available_seats = available_seats
#         self.name = name
#         self.l = l

#     def reserve(self, need_of_seats):
#         self.l.acquire()
#         self.l.acquire()
#         self.l.acquire()
#         print(F"Available seats are {self.available_seats}")

#         if self.available_seats >= need_of_seats:
#             name = current_thread().name
#             print(f"{need_of_seats} are allocated to {name}")
#             self.available_seats -= need_of_seats
#         else:
#             print("Sorry.. seats are not available.")
#         self.l.release()
#         self.l.release()
        
# b1 = Bus(2,"Ashoka travels", lock)

# t1 = Thread(target=b1.reserve, args=(2, ), name="Sushil")
# t2 = Thread(target=b1.reserve, args=(1, ), name="Sheetal")

# t1.start()
# t2.start()


#* What is need of R-lock:-

# from threading import *

# l = Lock()  #crashes program
# l = RLock()  


# def get_first_line():
#     l.acquire()
#     print("Fetching first line")
#     l.release()
    
# def get_second_line():
#     l.acquire()
#     print("Fetching second line")
#     l.release()
# def main():
#     l.acquire()
#     get_first_line()
#     get_second_line()
#     l.release()
    
# t = Thread(target=main)
# t.start()














"""
# Last thread synchronization technique #*Semaphore:-

In lock and R-lock at a time only one thread is allowed to execute.
But sometimes our requirement is to execute a particular number of threads #*i.e. =>3 threads at a time

Then you need semaphore to avoid race condition.

we create semaphore class ex in 3 steps

1. s = Semaphore()
2. s.acquire()   #You can use multiple acquire but you've to release them also
3. s.release()
"""

# Using semaphore:- 

# from threading import *
# obj = BoundedSemaphore()


# def display(name):
#     obj.acquire()
#     obj.acquire()
#     for i in range(5):
#         print("Jay shree ram")
#         print(name)
#         time.sleep(0.5)
#     obj.release()
#     obj.release()
#     obj.release()

# #creating thread
# t1 = Thread(target=display, args=('Thread-1',))
# t2 = Thread(target=display, args=('Thread-2',))
# t3 = Thread(target=display, args=('Thread-3',))
# t4 = Thread(target=display, args=('Thread-4',))
# t5 = Thread(target=display, args=('Thread-5',))

# #calling threads
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()





"""
When exceptions happens in multithreading then each threads has thier independant flow so exceptions happens
in which thread only that thread flow will be breaks otherwise another thread will flow simultaneosly.
"""

# import threading
# from time import sleep

# def custom_hook(args):
#     print("Exception occured in thread")
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])


# def display():
#     for i in range(4):
#         sleep(3)
#         print("hello: "+ 10)

# def show():
#     for i in range(5):
#         print("Hello")
#         sleep(0.5)
        
# threading.excepthook = custom_hook

# t1 = Thread(target=display)
# t2 = Thread(target=show)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# for i in range(10):
#     print("Sushil is smart 'Software Engineer'.")

