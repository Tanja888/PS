# Flexible Arguments
# Author: Tanja Juric

print ("Hi", 55, 343, [], {}, sep = ":") # keyword argument goes to the end

# flexible number of arguments

def flex1 (*args):
    print (type(args)) #it will show the type of class first - tuple
    for x in args:
        print (x)

flex1 (1, 2, 3, "hi", [])

# Multiple keyword arguments; call a function and give the name of the wanted argument
def flex2 (**kwargs):
    print (type(kwargs))
    for key, value in kwargs.items():
        print (f"{key} is {value}") #check this f

flex2 (age = 23, title = "hi")

# eg Calculate the average
def ave (*args):
    sumOfNumbers = sum(args)
    lenght = len(args)
    return sumOfNumbers/lenght

print(ave(2,3,4))

#or:
def ave (*args):
    sumOfNumbers = sum(args)
    lenght = len(args)
    return sumOfNumbers/lenght , sumOfNumbers

average , sumof = ave(3,4,5,6) #expand tuples to 2 things
print ("Average is", average, "Sum is", sumof)






