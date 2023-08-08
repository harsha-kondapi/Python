class Computer:
    # instance initializer or constructor or special method or __init__ method
    '''self is the parameter refers to the instance of a class
    and allows to access its attributes and
    other methods'''
    def __init__(self,cpu,ram):      # __init__ method is also a instance method of a class
        self.cpu = cpu      # instance variable
        self.ram = ram      # instance variable


    def config(self):       # instance method
        print("config is : ",self.cpu,self.ram)

# creating instance of class
com1 = Computer("i5",6)
com2 = Computer("Ryzen 3",8)

#Computer.config(com1)
#Computer.config(com2)

com1.config()  # calling instance method com1 object
com2.config()  # calling instance method com2 object

'''a = 5
#print(int.bit_length(a))
a.bit_length()'''