# In multithreading there are two objects:- 
# 1. Timer Object  2. Barrier Object.


#* 1. Timer Object

# import threading

# def task():
#     for i in range(3):
#         print("This is task is assigned to timer object of threading.")

# timer = threading.Timer(10, task)
# timer.start()

# for i in range(5):
#     print("Sushil you're best software engine.")



#* Barrier Object (Important object of multithreading mainly used for synchronization)

# This object allows threads to wait for each other at a specific point in their execution before proceeding further

import threading
import time

players_name = ['sushil', 'sayali', 'laxmi', 'shiv']

barrier = threading.Barrier(len(players_name))

def player(name):
    print(F"{name} started")
    score = 0
    for i in range(5):
        time.sleep(3)
        print(f"{name} is playing...")
    
    #barrier
    barrier.wait()
    score +=1
    print(f"{name} scored {score}")

    print(F"Sending winning amount into {name}")

Threads = []

for name in players_name:
    thread = threading.Thread(target=player, args=(name, ))
    Threads.append(thread)
    thread.start()
