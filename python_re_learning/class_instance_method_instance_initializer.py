class Myclass:

    # instance initializer or constructor or special method
    '''self is the parameter refers to the instance of a class
    and allows to access its attributes and
    other methods'''

    def __init__(self,name):            # instance method
        self.name = name

    def greet(self,ask):                    # instance method
        print(f"Hi {self.name}, {ask}")

# creating instance of a class
obj = Myclass("Rakesh")

# calling instance method
obj.greet("how are you doing ?")

