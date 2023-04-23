class Student:
    company = "Capgemini"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):     #accessor methods or getter
        return self.m1
    def set_m1(self,value):  #mutators methods or setter
        self.m1 = value
        return self.m1
    @classmethod
    def getCompany(cls):
        return cls.company
    @staticmethod
    def display():
        print("learning maths")

class Maths:
    def sum_of_two(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b
    def mul_of_two(self):
        self.x = 5
        self.y = 10
        return self.x * self.y
    def get_a(self):        #accessor methods or getter
        return self.a
    def set_b(self,value):      #mutators methods or setter
        self.b = value
        return self.b
    @staticmethod
    def info():
        print("Hi this is harsha")

s1 = Student(1,2,3)
s2 = Student(3,4,5)
s3 = Maths()
#s4 = Maths()


print(s1.m1,s1.m2,s1.m3)
print(s1.avg())

print(s1.get_m1())
print(s1.set_m1(1000))

Student.getCompany()
Student.display()

print(s3.sum_of_two(4,6))
print(s3.mul_of_two())

print(s3.get_a())
print(s3.set_b(20))

Maths.info()




