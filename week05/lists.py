# Lists
# Author: Tanja Juric

#list = [2, 4, 5, 6, "aa"]
#sum = 0
#for x in list:
    #sum = sum + x
    #print (x)

#for x in list:
    #sum += x
    #print (x)

l = [2, 4, 5, 6]
sum = 0
for x in l:
    sum += x
    print (sum)

# Shouldn't use range to iterate through the lists in Python:
#for i in range (0, len(l)):
    #print ("Value of index", i, "is", l[i])


names = ['Toni', 'Goga', 'Tea']
for name in names:
    #print ('Hello ' + name) #cannot concatenate integer to a string, we have no 3 in the list; comma instead of +
    print ('Hello ', name)


