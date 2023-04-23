class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

b1 = B()
b1.show()
