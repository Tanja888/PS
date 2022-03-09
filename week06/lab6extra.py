# Variables can be of type function
# We call those variables
# lists, tuples and dicts can have variables of type function in them 
# e.g. we could have a dict that stores the letter of the menu and the function associated with that letter
# we could access the function by that letter - not efficient, just easy to write

def fun1():
    print("This is fun1")

def fun2():
    print("This is fun2")

whichFun = fun1
whichFun()

whichFun = fun2
whichFun()