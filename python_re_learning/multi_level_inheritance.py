class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B(A):
    def __init__(self):
        print("in B init")

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

class C(B):
    def __init__(self):
        print("in C init")

    def feature5(self):
        print("feature 5 is working")

    def feature6(self):
        print("feature 6 is working")


#b = B()
c = C()
c.feature2()


