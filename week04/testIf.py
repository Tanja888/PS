# Trying the If statement
# Author: Tanja Juric

if False:
    # statements
    print ("Condition is true")

if 2 == 2:
    print ("Yes, the world is sane")

# easier than != example
b = 3
if b == 2:
    print ("b is equal to 2")
else:
    print ("b is not equal to 2")


a = 2
if a != 3:
    print ("I hope this is not displayed")
else:
    print ("2 is not equal to 2 is false")

aNumber = 5
if (aNumber % 2) == 0: #brackets for clarity
    print (aNumber, " is even")
elif (aNumber % 3) == 0: #if the number is even this won't be checked, if the 1st statement is true
    print (aNumber, "is divisable by 3")
else: 
    print (aNumber, "is not even or divisable by 3")

print ("This will always be outputted")
