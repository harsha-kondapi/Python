'''
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Example
If the number of arguments is unknown, add a * before the parameter name:
'''
def friend_names(*fnames):
    print(fnames[2] + " is backend developer")


friend_names("harsha", "rohith", "rakesh")

'''#Arbitrary Arguments are often shortened to *args in Python documentations.'''
