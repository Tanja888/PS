# test the module myFunctions
# test cases

import logging

logging.basicConfig(level=logging.ERROR)

#import myFunctions as mf
import myFunctions2 as mf

#print (mf.factorial(3))

print(mf.factorial(-10))
#assert mf.factorial(7) == 5040

print("All done") 

