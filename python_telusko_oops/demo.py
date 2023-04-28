class Computer:
    def __init__(self,cpu,ram):      #special method
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("config is : ",self.cpu,self.ram)

com1 = Computer("i5",6)   #constructor or object creation
com2 = Computer("Ryzen 3",8) #constructor or object creation

#Computer.config(com1)
#Computer.config(com2)

com1.config()  #object calling
com2.config()  #object calling

'''a = 5
#print(int.bit_length(a))
a.bit_length()'''