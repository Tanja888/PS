# More on files

# check if the file exists
# importing os.path and isfile() function
# os.path.isfile() method
# https://www.geeksforgeeks.org/python-os-path-isfile-method/

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print ("File does not exist")

# try/catch loop
def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0
