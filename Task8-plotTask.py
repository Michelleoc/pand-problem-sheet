# Topic 'Looking ahead' - Weekly Task 08
# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author : Michelle O'Connor

import numpy as np
import matplotlib.pyplot as plt

# Passed array in similar to how we did in the week 08 lectures
x = np.array([0,4])

# insert functions as outlined in the task 
# using **2 for squared 4*4
# using **3 for cubed 4*4*4
f =x
g =x**2
h =x**3

# Plotting f, g & h functions separately
# https://stackoverflow.com/questions/22276066/how-to-plot-multiple-functions-on-the-same-figure-in-matplotlib
plt.plot(f, 'r') # red line
plt.plot(g, 'b') # blue line
plt.plot(h, 'g') # green line

# formatting the plot 
# https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/introduction-to-matplotlib-plots/customize-plot-colors-labels-matplotlib/
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html

plt.plot(title = "Function Plot",
       xlabel = "X Axis", 
       ylabel = "Y Axis")

# passing the legend names in a list
# https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html

plt.legend(['f(x)=x', 'g(x)=x2', 'h(x)=x3'])

plt.savefig("Weekly_Task_Plot.png")

plt.show()


# https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
# https://stackoverflow.com/questions/22276066/how-to-plot-multiple-functions-on-the-same-figure-in-matplotlib