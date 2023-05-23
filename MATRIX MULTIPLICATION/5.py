# 2D TRANSFORMATION MATRICES

import numpy as np
import matplotlib.pyplot as plt

# 2D input vector
v = np.array([3, -2])

# 2x2 transformation matrix
A = np.array([[1, -1], [2, 1]])

# output vector is Av (convert v to column)
w = A @ np.matrix.transpose(v)


# plot them
plt.plot([0, v[0]], [0, v[1]], label="v")
plt.plot([0, w[0]], [0, w[1]], label="Av")

plt.grid()
plt.axis((-6, 6, -6, 6))
plt.legend()
plt.title("Rotation + stretching")
plt.show()
