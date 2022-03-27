# Weekly Task 08 - Write a program that displays a plot of the functions:
# f(x)=x, g(x)=x**2 and h(x)=x**3 in the range [0,4] on one set of axes
# Author: Tanja Juric

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig, ax = plt.subplots()

x = np.array(range(0,4))
g = x * x
h = x ** 3


# First I did the legend but realized that the labels for each line looked nicer
plt.plot(x, x, color = "purple")
plt.plot(x, g, color = "green")
plt.plot(x, h, color = "orange", linestyle = "dashed", linewidth = 1.5)

'''
plt.plot(x, x, label = "x", color = "purple")
plt.plot(x, g, label = "xsquared", color = "green")
plt.plot(x, h, label ="xcubed", color = "orange", linestyle = "dashed", linewidth = 1.5)
'''
plt.xlabel("X - values", fontsize=8)
plt.ylabel("Results", fontsize=8)
plt.title("Functions plot", fontsize=10)
#plt.legend()
#fontfamily="sans-serif"

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.text(x=2.3, y=23, s="xcubed", color="orange")
ax.text(x=2.8, y=10.1, s="xsquared", color="green")
ax.text(x=2.9, y=3.56, s="x", color="purple")
#ax.text(s="Functions plot", x=1.08, y=15.9)
plt.subplots_adjust(left=0.1, bottom=0.2, right=None, top=None, wspace=None, hspace=None)

ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['0', '1', '2', '3'], fontsize=8)
ax.set_yticks([0, 10, 20, 30])
ax.set_yticklabels(['0', '10', '20', '30'])

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.show()

# Little bit on plotting:
# URL https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# Wanted to remove outside borders:
# URL https://stackoverflow.com/questions/22082111/how-to-despine-a-matplotlib-and-seaborn-axes
# Was annoyed with x label not showing properly so I used subplot adjust:
# URL https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
# URL https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html
# Adding labels on the lines and changing the ticks:
# https://towardsdatascience.com/a-beginners-guide-to-plotting-fivethrityeight-like-visualizations-5b63d3f3ddd0
# On fontsize of ticks:
# URL https://stackoverflow.com/questions/6390393/matplotlib-make-tick-labels-font-size-smaller
# To move a title:
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html
# Officially fell into a rabbit hole with this task



