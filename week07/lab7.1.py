# Non-existent file
# Author: Tanja Juric

# Nothing will happen, the file doesn't exist; if it was existent we would have to add r mode too to read it
#with open ("text-a.txt") as f:
    #data = f.read()
    #print(data)

# with statement automatically closes the file when it is finished with it
# data = f.write ("test b\n")  - write function returns the numbers of characters including the new line
with open ("test-b.txt", "w") as f:
    data = f.write ("test b\n") 
    print(data)

with open ("test-b.txt", "w") as f2:
    data = f2.write("another line\n")    # the content of test-b-txt is "another line" because we overwritten the previous content with w
    print(data)

with open ("test-d.txt", "w") as f:
    data = f.write ("test d\n")
    print(data)

with open ("test-d.txt", "a") as f2:           # the content was not overwritten because we opened the file in append mode
    data = f2.write ("another line\n")
    print(data)
 