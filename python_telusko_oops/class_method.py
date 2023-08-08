class Student:

    @classmethod
    def details(cls,name,age):
        cls.name = name
        cls.age = age
        print(cls.name,cls.age)


s1 = Student.details("harsha","23")

#s1 = Student()
#s1.details("harsha","23")

