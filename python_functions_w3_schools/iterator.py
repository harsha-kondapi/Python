mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))

'''for x in myit:
    print(x)'''

mystr = "banana"
myiterator = iter(mystr)

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))

'''for x in myiterator:
    print(x)'''