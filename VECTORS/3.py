# Vector-Scalar Multiplication

import numpy as np
import matplotlib.pyplot as plt

# In Linear Algebra, matrix is indicated as uppercase letters like 'A', 'M', 'C', Vectors are indicated as lowercase
# letters like 'v', 'u', 'w' and Scalar numbers are typically indicated as lowercase, non-boldfaced greek letters.

# vector and scalar
v1 = np.array([3, -1])
l = 2.3
v1m = v1 * l  # scalar-modulated

# plot them
plt.plot([0, v1[0]], [0, v1[1]], "b", label="$v_1$")
plt.plot([0, v1m[0]], [0, v1m[1]], "r:", label="$\lambda v_1$")

plt.legend()
plt.axis("square")
# make the limits dynamic
axlim = max([max(abs(v1)), max(abs(v1m))]) * 1.5  # dynamic axis lim
plt.axis((-axlim, axlim, -axlim, axlim))
plt.grid()
plt.show()

# NOTE: Vector-Scalar multiplication changes the length but preserves the direction!
