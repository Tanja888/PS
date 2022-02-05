# Learning variables types
# Author: Tanja Juric

ageOfPatient = {}
age = '3'

# converting type into str to concatenate it to the message
# this is called 'type casting'
print ("type of ageOfPatient is: " + str(type(ageOfPatient)))
print ("type of age is: " + str(type(age)))

print ("You are " + str(age) + " years old.")
nextYear = int(age) + 1
print ("Next year you will be " + str(nextYear))

