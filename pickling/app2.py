import pickle

f = open('data.dat', 'rb')

while True:
    try:
        obj = pickle.load(f)
        obj.display()
    
    except EOFError:
        print('all data unpickled.')
        break
    
f.close()