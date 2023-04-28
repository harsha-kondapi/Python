class Student:

    school = "SPMS"

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("learning")

s1 = Student()
print(Student.getSchool())

Student.info()