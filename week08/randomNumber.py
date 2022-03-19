# Random number generator
# Author: Tanja Juric

import numpy as np

randomNumbers = np.random.randint(100, 200, 5)
print(randomNumbers)

# normal distribution, for graphs
randomNumbers = np.random.normal(size = 100)
print(randomNumbers)

# good for manipulating a lot of data: matrices, arrays