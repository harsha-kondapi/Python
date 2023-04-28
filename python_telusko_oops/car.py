class Car:
    wheels =   #class namespace, static variable
    def __init__(self):
        self.com = "BMW"  #instance namespace,instance variable
        self.mil = 10     #instance namespace,instance variable

c1 = Car()
c2 = Car()

c2.mil = 8

Car.wheels = 5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,Car.wheels)