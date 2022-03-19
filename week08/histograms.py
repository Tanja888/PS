# Histograms
# Author: Tanja Juric

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)  #it will generate the same random numbers; plot will look the same; for debugging
normData = np.random.normal(size=10000)

plt.hist(normData)
plt.show()

# pie chart
fruit = np.array(['Apples', 'Orange', 'Banana'])
numbers = np.array([23,77,100])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()