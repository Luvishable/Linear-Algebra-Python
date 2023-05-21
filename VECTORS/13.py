# Interpreting and Creating Unit Vector

import numpy as np
import matplotlib.pyplot as plt

# vector
v1 = np.array([-3, 6])

# mu
mu = 1 / np.linalg.norm(v1)

v1_unit = v1 * mu

# plot them
plt.plot([0, v1_unit[0]], [0, v1_unit[1]], "r", label="v1-norm", linewidth=5)
plt.plot([0, v1[0]], [0, v1[1]], "b", label="v1")

# axis square
plt.axis("square")
plt.axis((-6, 6, -6, 6))
plt.grid()
plt.legend()
plt.show()

# As can be seen, to find the unit vector we need to multiply the vector with a mu value. We extract mu from the norm
# of the vector.
