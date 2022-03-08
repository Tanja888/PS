# Anonymous functions

#def doubler (num):
    #return num * 2

#def tripler (num):
    #return num * 3

#functions equal to variables

isMax = True
if isMax:
      fun = lambda num : num * 2     # nicer than: fun = doubler; anonymous fn, it doesn't have a name 
else:
    fun = lambda num : num * 3

var = fun (10)
print (var)


# sorted
list = [22, 33, 11, 1, 44]
print (list)
newList = sorted (list)
print (newList)


data = [{'first': 'Guido', 'last': 'Von Rossum', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Hopper',     'YOB': 1906},
        {'first': 'Alan', 'last': 'Turing',      'YOB': 1912}]
        
#def sortFun(item):
    #print ("in sortFun")
    #return item ['YOB']

#print (data)
newData = sorted(data, key = lambda item : item['last'])       #key = sortFun
print (newData)
for item in newData:
    print (item)

