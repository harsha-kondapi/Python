class School:

    school_name = "SPMS"        # class variable
    location = "Nacharam"       # class variable

    @classmethod
    def getSchool(cls):
        return (cls.school_name,cls.location)

    @staticmethod
    def student_details(name,age):
        return (name,age)

    def student_info(self,name,age,height):
        self.name = name            # instance variable
        self.age = age
        print(self.name,self.age,height)


s1 = School()
print(s1.getSchool())
print(s1.student_details("harsha",15))
s1.student_info("rakesh",15,6)