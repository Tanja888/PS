# Write a program that plots histogram of the salaries in 8.1

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1) # we seeded the random number generator, random numbers will always be the same, easier to debug
salaries = np.random.randint(minSalary,maxSalary,numberOfEntries)

plt.hist(salaries)
plt.show()