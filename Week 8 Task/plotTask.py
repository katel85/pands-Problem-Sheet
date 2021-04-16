# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Catherine Leddy 


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 4.0, 0.5) # three arguments- starting value, ending value and step size between them)
f = x      
g = x**2   
h = x**3 

plt.plot(f,f, '-m', marker='o', label = 'f(x)=x')  
plt.plot(f,g, '--b', marker= 'x',  label = 'g(x)= x2')
plt.plot(f,h, '-.g', marker= 's', label = 'h(x)=x3')
plt.ylabel('Y-AXIS')
plt.xlabel('X-AXIS')
plt.title ('Functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] ')
plt.legend()
plt.show()



# Ref : https://sweetcode.io/visualizing-data-python-matplotlib/
# Ref : https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# Ref: https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible
# Ref : https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
# Ref : https://matplotlib.org/3.1.1/tutorials/intermediate/legend_guide.html
# Ref : https://e2eml.school/matplotlib_points.html




