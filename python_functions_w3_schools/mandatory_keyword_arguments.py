def name_tag(fname,lname,*args,title='',**kwargs):
    print(title,fname,lname,args,kwargs)

name_tag("harsha","kondapi","rohith","vijay",title="analyst",friend="rakesh")


'''There are situations where you will want to use mandatory keyword arguments without accepting 
an arbitrary number of positional arguments. To support this, Python allows you to omit the 
name of the *args argument. The arguments following the asterisk can only be passed to the 
function as keyword arguments, but Python will not allow you to pass extra positional arguments 
to the function.'''
def tag(first_name,last_name,*,title=''):
    print(first_name,last_name,title)

tag("damon","salvatore","stefen",title="vampire_dairies")