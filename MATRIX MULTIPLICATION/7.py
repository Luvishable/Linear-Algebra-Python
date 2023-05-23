# GEOMETRIC TRANSFORMATIONS VIA MATRIX MULTIPLICATIONS

import numpy as np
import matplotlib.pyplot as plt

# In this lesson, we are gonna transform a circle by multiplying it with a matrix and see how we can rotate a circle

# generate XY coordinates for a circle
x = np.linspace(-np.pi, np.pi, 100)
xy = np.vstack((np.cos(x), np.sin(x))).T

# plot the circle
plt.plot(xy[:, 0], xy[:, 1], "o")

# create a 2x2 matrix
T = np.array([[1, 2], [2, 1]])

# multiply matrix by coordinates
newxy = xy @ T

# plot the new coordinates
plt.plot(newxy[:, 0], newxy[:, 1], "o")

plt.axis("square")
plt.show()
