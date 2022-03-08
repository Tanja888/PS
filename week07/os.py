# OS module for Files

# Check if file exists, delete files
import os

filename = 'test.txt'
if os.path.exists(filename):
    print (filename, "already exists")
    os.remove(filename)
else:
    print (filename, "does not exist, do you want to create it?")

