# Writing a program that subtracts two numbers
# Author: Tanja Juric

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
result = x - y

# can be done in both ways
print (str(x) + ' minus ' + str(y) + ' is ' + str(result))
print ('{} minus {} is {}' .format(x, y, result))


