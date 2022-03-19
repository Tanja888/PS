# Matplotlib
# Author: Tanja Juric

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints


plt.plot(xpoints, ypoints, label = "xsquared")
plt.plot(xpoints, xpoints, label = "straight", color = "blue")
plt.legend()
#plt.show()
#plt.savefig('firstPlot.png')  #to save the plot; cannot save with show before it


randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label = "random")
plt.legend()
plt.show()

