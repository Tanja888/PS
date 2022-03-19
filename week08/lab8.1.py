# 8.1. Write a program that makes a list, called salaries, that has 10 random numbers (20000 - 80000)
# Author: Tanja Juric

import numpy as np

#salaries = np.random.randint(20000, 80000, 10)
#print(salaries)

# better to put absolute values set into variables at the beginning of the program
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # we seeded the random number generator, random numbers will always be the same, easier to debug
salaries = np.random.randint(minSalary,maxSalary,numberOfEntries)
salariesPlus = salaries + 5000
salariesPercent = salaries * 1.05  #increases all the salaries by 5% 
newSalaries = salariesPercent.astype(int)

print(salaries)
print(salariesPlus)
print(salariesPercent)
print(newSalaries)