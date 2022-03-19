# Numpy
# Author: Tanja Juric

import numpy as np

listOfNumbers = [1,2,3,6]     # lists will have commas
numbers = np.array([1,2,4,5]) # arrays without commas

#listOfNumbers = listOfNumbers + 3    # cannot concatenate int to list
# numpy allows the calculation, will add to every number
#numbers = numbers + 3   
#numbers = numbers * 3   

# useful for matrices
numbers = numbers * np.array([1,4,5,6]) #multiplies with [1,2,4,5]

print(listOfNumbers)
print(numbers)

