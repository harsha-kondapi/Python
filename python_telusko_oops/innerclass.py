class Student:
    def __init__(self):
        self.name = 'Ramu'
        self.age = 25
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.cpu, self.ram)


s1 = Student()

s1.show()
