"""
Thread communication:- 
In concurrent programming sometimes we need to co-ordinate threads.
Threads communicate with each othre via signals.

3 ways to communicate:-
1. by creating event object
2. by creating condition object
3. by using queue module
"""

# way 1. Using event:- 


# import threading
# import time

# e = threading.Event()

# def task():
#     print("Game started")
#     time.sleep(3)
#     e.set()

# def end():
#     e.wait()
#     if e.is_set():
#         print('Destroying session')

    

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=end)

# t1.start()
# t2.start()




"""
*Condition object:-

but when multithreads working then event objects confused then thats why python introduced
Condition object.
To communicate between multiple threads.

Condition object gives multiple methods:- acquire, release, wait, notify, notify_all()

These methods must only be called when the calling thread has acquired the lock. 
"""



# import threading
# import time


# def write_temp_data():
#     con.acquire()
#     with open('report.txt', 'w') as file1:
#         days = ['Monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#         for day in days:
#             temp = input(f"Enter the temperature for {day}: ")
#             file1.write(temp + '\n')
#     con.notify_all()
#     con.release()

# def max_temp():
#     con.acquire()
#     con.wait(timeout=0)
#     with open('report.txt', 'r') as file1:
#         data = file1.readlines()
#         max_val = float(data[0].strip('\n'))
#         for val in data[1:]:
#             val = float(val.strip("\n"))
#             if val > max_val:
#                 max_val = val
#     print("The maximum temperature is: ",max_val)
#     con.release()


# def avg_temp():
#     con.acquire()
#     con.wait(timeout=0)
#     with open('report.txt', 'r') as file1:
#         data = file1.readlines()
#         sum1 = 0
#         for val in data:
#             val = float(val.strip("\n"))
#             sum1 = sum1 + val
#         avg = sum1 / len(data)
#         print("The average temperature of week: ", avg)
#     con.release()

# con = threading.Condition()

# t1 = threading.Thread(target= write_temp_data)
# t2 = threading.Thread(target= max_temp)
# t3 = threading.Thread(target= avg_temp)

# t1.run()
# t2.run()
# t3.run()








#* Queue object in python:- 

from threading import Thread
from queue import Queue

def producer(my_que):
    print("Producer running...")
    n = int(input("Enter number of students: "))

    for i in range(n):
        marks = float(input("Enter marks: "))
        my_que.put(marks)
    my_que.put(None)

    print("Producer end.")

def consumer(my_que):
    print("Consumer running...")
    while True:
        item = my_que.get()    
        if item is None:
            break
        print(f"Consumer got {item}")
    print("Consumer end.")

my_que = Queue()

t1 = Thread(target=producer, args=(my_que, ))
t2 = Thread(target=consumer, args=(my_que, ))

t1.start()
t2.start()