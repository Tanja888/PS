# Write a program that makes a list called ages that has the same number random values as salaries
# Range 21 to 65
# Make scatter plot

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100 

ageYoung = 21
ageOld = 65

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(ageYoung, ageOld, numberOfEntries) #could be(ageYoung=21, ageOld=65, size=numberOfEntries)

print(salaries)
print(ages)

plt.scatter(ages, salaries, label="Salaries") # add a legend, title and axis labels to the plot
#plt.show()

#add x squared
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints
plt.plot(xpoints, ypoints, color='r', label="X squared")

plt.title("Random plot")
plt.xlabel("Age")
plt.ylabel("Salaries")
plt.legend()
#plt.show()
plt.savefig("Prettier-plot.png")











