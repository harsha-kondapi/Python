import pickle

unpic = open('pickle_details.txt','rb')
m = pickle.load(unpic)  # unpickling
print(m)