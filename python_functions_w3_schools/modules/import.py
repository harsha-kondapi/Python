import mymodule,platform

#here platform is a built-in module

mymodule.greeting("rakesh")
#mymodule.greeting(mymodule.person1["name"]+" I am living in "+mymodule.person1["country"])

a = mymodule.person1["age"]
print(a)

x = platform.system()
print(x)

#
print(dir(mymodule))

help(mymodule.greeting)
help(mymodule.person1)
