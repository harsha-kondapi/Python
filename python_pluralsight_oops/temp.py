class Acc:
def __init__(self, id):
self.id = id
id = 555

acc = Acc(111)
print(acc.id)

2.)
def f(v, values):
v = 1
values[0] = 44

t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

3.)
d = {"john":40, "peter":45}
del d["john"]

4.)
def f(a = 1, b = 1, c = 2):

5.)
__rmul__(self,other)

6.)
def main():
try:
f()
print("After the function call")
except ZeroDivisionError:
print("Divided by zero!")
except:
print("Exception")

def f():
print(1 / 0) main()

7.)
any([5>8, 6>3, 3>1])

8.)
def foo(*p):
print(p)

foo(2,1,3)

9.)
_ = '1 2 3 4 5 6'
print(_)

10.)
dictionary = {}
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1

sum = 0
for k in dictionary:
sum += dictionary[k]

print (sum)

















dictionary = {}
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1

sum = 0
for k in dictionary:
    sum += dictionary[k]

print (sum)