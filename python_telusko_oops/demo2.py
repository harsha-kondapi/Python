class Student:
    def details(self):      # instance method of a class
        self.name = "harsha"
        self.age = 23
        print(self.name,self.age)

# creating instance of a class
s1 = Student()

# calling instance method of class
s1.details()
#print(s1.name,s1.age)
