# Try except

#filename = 'data.txt'

import sys    #check if directories exist

#print(sys.argv) #will get a list with the name of a file; argv gives what comes inside the list; useful for debugging
#filename = 'notthere.txt'
filename = sys.argv[1]  #element 1; in this case ['.\\tryexcept.py', 'test'] test is the element 1

try:
    with open(filename) as f:
        print(f.read())
    var = 10/0
#except FileNotFoundError: or
except FileNotFoundError as e:
    #print("File (", filename, ") does not exist", sep='')
    print(e)
#except:
    #print("an Exception occurred")

print("The End")
# when I run python .\tryexcept.py data.txt, I will get ['.\\tryexcept.py', 'data.txt']
# data.txt is the first argument but is the second thing in the list




