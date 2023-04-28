class A:
    def __init__(self):
        print("A init")
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")


class B(A):
    def __init__(self):
        #super().__init__()
        print("B init")
    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")


class C(B,A):
    def __init__(self):
        super().__init__() #overriding base class  dunder init method explicitly, explicit is better than implicit
        print("C init")
    def feature5(self):
        print("feature 5 is working")

    def feature6(self):
        print("feature 6 is working")



'''a1 = A()
a1.feature2()'''
'''b1 = B()
b1.feature1()'''
c1 = C()
c1.feature1()
