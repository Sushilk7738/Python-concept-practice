"""
types of threads:- 
1. non daemon threads (non-supportive threads)
2. daemon threads (supportive threads)


*Daemon threads:- Daemon threads are continuously runs in background and provide supports to non daemon threads.
*when all non daemon threads gets terminated automatically daemon thread also get terminated.

Daemon threads are often used for tasks such as monitoring, background services , or 
Cleanup operations.
"""

# Checking daemon nature of main thread:-

# from threading import * 
# obj = current_thread()
# obj.daemon = True
# print(obj.daemon)  #returns false

#* You cannot change the running thread daemon nature



#* How to change the daemon nature of main_thread

# from threading import * 

# def display():
#     print("The name is Sushil.")
#     t2 = Thread(target=demo)
#     print("The daemon nature of t2 is: ", t2.daemon)   #daemon nature by default inherited from parents.

# def demo():
#     print("Something")

# t1 = Thread(target=display)
# # print("Daemon nature of t1: ",t1.daemon)
# t1.daemon = True
# t1.start()
# print("Daemon nature of t1: ", t1.daemon)    #returns true




#* Daemon theads examples:-

from threading import *
from time import sleep


# def display():
#     for i in range(1, 11):
#         print("Teaching session: ", i)
#         sleep(0.1)

# t1 = Thread(target=display)
# t1.daemon = True
# t1.start()

# sleep(3)
# print("Exam time!")
# print("Exam over..")