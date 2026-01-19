# import pickle
# unpickling
# f1 = open('abc.xyz', 'rb')
# data = pickle.load(f1)
# print(data)




import picklingun , pickle

f = open('data.dat', "wb")
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll: "))
    marks = float(input("Enter marks: "))
    obj = picklingun.Student(name, roll , marks)

    pickle.dump(obj, f)   #pickling
    
print('objects stored successfully')
