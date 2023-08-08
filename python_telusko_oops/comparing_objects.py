class Person:
    def __init__(self):     # __init__ method or special method or instance initializer or constructor
        self.name = "harsha"
        self.age = 23

    def update(self):       # instance method
        self.name = "rohith"
        self.age = 25
    def compare(self,c2):   # instance method
        if self.age == c2.age:
            return True
        else:
            return False

# creating a instance of a class
c1 = Person()
c2 = Person()

'''c2.name = "rakesh"
c2.age = 24
'''
c2.update()

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")

print(c1.name,c1.age)
print(c2.name,c2.age)

