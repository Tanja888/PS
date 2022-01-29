# Uses a variable to greet
# Author: Tanja Juric

name = "Tanja"
print ('Hello ' + name)

age = 34
# print ('Your age is ' + age) - doesn't work because it's not the same variable type

# Shows different ways of formatting:
print ('Your age is ' + str(age))
print ('Your age is {}'.format(age))
print ('Hello {} \tYour age is {}' .format (name, age))