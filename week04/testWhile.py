# While loops
# Author: Tanja Juric

# While condition
    # Statements

count = 0
while count < 10:
    print (count)
    count += 1

count = 10
while count >= 0:
    print (count)
    count -= 1
print ("Blast OFF")

val = input ("Enter something (q to quit): ")
while val != 'q':
    print ("You said: " + val)
    val = input ("(q to quit): ")
print ("Goodbye")


# Example of an infinite loop
# we have to change the variable we are working with into condition 
count = 0
while count < 10:
    print (count)
    county = count + 1
