import pickle

details = {'name':'harsha','password':'harsha123'}

with open('pickle_details.txt','wb') as f:
    pickle.dump(details,f)  #pickling