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