# Variable scope

x = 7

def topower (number, power = 3):  #shouldn't use global variables but ones that are arguments or inside the function
    x = 3
    print ("In function x is", x) #cannot put print before x, 1st we have to assign x 
    return number ** power

# can be like this, use global var x
def topower (number, power = 3): 
    global x
    print ("In function x is", x) 
    x = 3
    return number ** power


topower (4)
print ("Outside function x is", x)

# Classes instead of global variables