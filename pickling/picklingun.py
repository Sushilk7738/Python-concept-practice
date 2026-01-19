"""
*python objects to converted into bytestring is called "pickling" or "serialization"

*and converting that bytestream to python objects is called "unpickling" or deserialization.

we use "pickle" module to perform this operations => 

*when we want to pickle from py to byte => use dump() it stores data with file if u dont want
*file then use dumps()

*when we want to unpickle from byte to py => use load() it converts data and stores into file
*but if u dont want file then use loads()


""" 



import pickle

data = ["Sushil", 98.2, 25]

#pickling

byteData = pickle.dumps(data)
# print(byteData)        #pickled representation(bytestream)

#unpickling

pythonData = pickle.loads(byteData)
# print(pythonData)      #unpickled representation(python object)



fruits = ['apple', 'grapes', 'orange']

#pickling

# f = open("abc.xyz" , 'wb')
# pickle.dump(fruits, f)

# f.close()


class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name is {self.name}\nRoll no is '{self.roll}'\nMarks is {self.marks} ")
        


