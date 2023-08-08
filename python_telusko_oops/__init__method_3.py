class Student:

    def __init__(self,college,branch):
        self.name = "Harsha"
        self.age = 23
        self.college = college
        self.branch = branch

    def personal_details(self):
        print(self.name,self.age)

    def college_details(self):
        print(self.college,self.branch)

s1 = Student("NNRG","CSE")
s1.personal_details()
s1.college_details()
