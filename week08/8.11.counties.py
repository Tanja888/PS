# Write a program that has a list of counties, make it a long list (pick from five counties)
# Make some counties appear more than others
# Make a pie chart of the counties

# Making a pie plot of the unique occurences of values in an array

import numpy as np
import matplotlib.pyplot as plt

# array of occurences 
possibleCounties = ['Cork', 'Galway', 'Dublin', 'Donegal', 'Sligo']
# pick 100 randomly from possible counties 
counties = np.random.choice( 
    possibleCounties,
    p = [0.1, 0.4, 0.1, 0.12, 0.28],  # frequency
    size = (100)
)

# number of occurences of each county
# tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)

#plt.pie(counts, labels = unique)
plt.bar(unique, counts)
plt.show()