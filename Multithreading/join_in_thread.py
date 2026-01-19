from threading import Thread, current_thread
import time

def upload():
    print("Uploading start")
    print(current_thread().name)
    # time.sleep(3)
    print("Video Uploaded")

def notification():
    print("Sending notification to subscribers to watch the video")
    print(current_thread().name)
    # time.sleep(2)


# t1 = Thread(target=upload)
# t2 = Thread(target=notification)

# t1.start()
# t1.join()
# t2.start()
# t2.join()

#main thread code

# for i in range(5):
#     print(f"{i} million views")
#     print(current_thread().name)


"""
so when to use join method in thread if a thread wants to wait for some other thread then
we should go for join() method
"""




# Why to use multithreading:-
# a function with multithreading: -

from threading import Thread
import time

def square(n):
    print(f"Finding the square of {n}...")
    time.sleep(1)
    print(f"The square of {n} is: {n*n}")

def cube(n):
    print(f"Finding the cube of {n}...")
    time.sleep(1)
    print(f"The cube of {n} is : {n*n*n}")

begin = time.time()

# t1 = Thread(target=square, args=(2, ))
# t2 = Thread(target=cube, args=(3, ))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"Total time taken: {time.time() - begin }")


# a function without multithreading:- 


def square(n):
    print(f"Finding the square of {n}...")
    time.sleep(1)
    print(f"The square of {n} is: {n*n}")

def cube(n):
    print(f"Finding the cube of {n}...")
    time.sleep(1)
    print(f"The cube of {n} is : {n*n*n}")

# begin = time.time()
# square(3)
# square(2)

# print(f"Total time taken: {time.time() - begin }")

"""
the answer is multithreading is much efficient and faster than normal programming
this proven in above example

"""


