'''Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

Example'''

def my_function(country = "norway"):
    print("I am from "+country)

my_function("sweden")
my_function("India")
my_function()
my_function("US")