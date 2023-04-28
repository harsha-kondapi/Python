class A:
    def sum(self):
        self.a = 4
        self.b = 6
        return self.a + self.b

class B(A):
    def mul(self):
        return self.a * self.b


a1 = A()
print(a1.sum())
print(a1.a,a1.b)

b1 = B()
print(b1.sum())
