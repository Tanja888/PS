# Tuples
# Author: Tanja Juric

# like lists but not changeable

t = (1, 2, 3) #can be without brackets too 
print (t)

print (len(t))
print (t[0]) #index

#cannot append anything

#Unpacking tuples
x = 0.125
print (x.as_integer_ratio ())

numerator, denominator = x.as_integer_ratio()
print ("", numerator, "/", denominator) #commas change the variable types

x, y, z = t
print (x)
print (z)



