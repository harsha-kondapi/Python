class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c
            return s
        elif a != None and b != None:
            s = a + b
            return s


s1 = Student(58, 69)
print(s1.sum(4, 6))