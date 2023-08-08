class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2-A is working")

class B:
    def __init__(self):
        print("in B init")

    def feature2(self):
        print("feature 2-B is working")

    def feature3(self):
        print("feature 3 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("in C init")

    def feature5(self):
        print("feature 5 is working")

    def feature6(self):
        print("feature 6 is working")

    def feat(self):
        super().feature1()


#b = B()
c = C()
c.feature2()
c.feat()
c.feature3()


