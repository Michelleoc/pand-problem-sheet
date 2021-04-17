# Topic 'Looking ahead' - Weekly Task 08
# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author : Michelle O'Connor

import numpy as np
import matplotlib.pyplot as plt

# The below 3 lines represent ways to pass in the range [0,4]
# https://realpython.com/how-to-use-numpy-arange/

x = np.array([0,1,2,3,4]) 
# x = np.arange(5, dtype=int)
# x = np.arange(0,5) # returns 0,1,2,3,4

# Inserted functions as outlined in the task 
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

# putting the legend names in a list
# https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html
# location of the legend
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# creating a grid effect
# https://matplotlib.org/2.0.2/api/pyplot_api.html


plt.legend(['f(x)=x', 'g(x)=x2', 'h(x)=x3'], loc=0)
plt.title("Function Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

# saving the plot as a png file
plt.savefig("Weekly_Task_Plot.png")

# Displaying the plot
plt.show()


# https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html

