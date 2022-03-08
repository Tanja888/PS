# Files

# Creating a test.txt file with the Hello World content
# wt is the mode
# filename is the path
# better to do read or write, not together
# w will delete the previous content of the file

filename = 'test.txt'
with open(filename, 'w+t') as f:
    f.write("Hello World2")      
    f.seek(0)          # went to the beginning of the file
    data = f.readline()
    print(data)

print ("Done")        

'''
# cannot read a file if it doesn't already exist
filename = 'testread.txt'
with open (filename, 'r') as f:
    data = f.read()
    print (data)
'''

# for large files read one line at a time
with open ('files.py', 'rt') as f:
    for line in f:
        #print (line[:-1])     # last character is a new line so we delete that one with :-1
        print (line, end="")   # doesn't print a new line




