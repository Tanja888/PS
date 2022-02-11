# Division and remainder
# Author: Tanja Juric

firstNo = int (input("Please enter the number you want to divide: "))
secondNo = int (input("Please enter the number you want to divide by: "))

division = firstNo // secondNo  # // gives the integer division
remainder = firstNo % secondNo  # % gives the remainder
print ('{} divided by {} is {} with remainder {}' .format (firstNo, secondNo, division, remainder)) 


