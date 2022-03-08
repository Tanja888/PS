# Files 2
# Author: Tanja Juric

# write a program that counts how many times it was run 

# a)
# write a function that reads in a number from the file
# test the program by calling a function and outputting the number

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

num = readNumber()
print (num)

#b)
# write a function that takes in a number and overwrites a file with that number (count.txt)
filename = "count.txt"
def writeNumber(number):
    with open (filename, "wt") as f:
     f.write(str(number))

writeNumber(3)

# c) write a program that uses previous two functions to count how many times the program has been run
# check that number goes up each time

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open (filename, "wt") as f:
     f.write(str(number))

num = readNumber()
num += 1
print ("We have run this program {} times" .format(num))
writeNumber(num)

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print ("File does not exist")
    writeNumber(0)

# try/catch loop
def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0

