# Variables and State Lab 3.1
# Author: Tanja Juric

i = 5
fl = 3.14
bool = False
greet = 'Hello Again'
ls = []

# Using type function to determine variable types

# just realized I can put comma instead of + in a code
print ('Your variable i is of type: ' + str(type(i)) + ' and value: ' + str(i))
print ('Your variable i is of type:', str(type(i)), 'and value:', str(i))

# like in the lab solution; using format instead of type casting
print ('Your variable {} is of type: {} and value: {}' .format ('i', type(i), i))
print ('Your variable {} is of type: {} and value: {}' .format ('fl', type(fl), fl))
print ('Your variable {} is of type: {} and value: {}' .format ('bool', type(bool), bool))
print ('Your variable {} is of type: {} and value: {}' .format ('greet', type(greet), greet))
print ('Your variable {} is of type: {} and value: {}' .format ('ls', type(ls), ls))