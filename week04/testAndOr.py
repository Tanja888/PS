# And, or
# Author: Tanja Juric

number = 12
if ( number >= 0 ) and ( number <= 100 ):
    print ("Valid")

if (number <= 0) or (number >= 100):
    isbad = True
    print ("Stop")
else:
    isbad = False
    print ("Go")