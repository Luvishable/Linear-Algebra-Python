# SPAN

import numpy as np
import matplotlib.pyplot as plt

# Span is almost the same thing as subspace but the terms are used to imply slightly different concepts.

# Subspace is a region of space that you can reach by any linear combination of the given vectors. Those vectors span
# that subspace, formally the span of a set of vectors.

# Span also stretches to infinity

# For more explanation about span: https://mikebeneschan.medium.com/how-to-understand-span-linear-algebra-cf3baa12edda

# set S
S1 = np.array([1, 1, 0])
S2 = np.array([1, 7, 0])

# vectors v and w
v = np.array([1, 2, 0])
w = np.array([3, 2, 1])

# draw vectors
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot([0, S1[0]], [0, S1[1]], [0.1, S1[2] + 0.1], "r", linewidth=3)
ax.plot([0, S2[0]], [0, S2[1]], [0.1, S2[2] + 0.1], "r", linewidth=3)

ax.plot([0, v[0]], [0, v[1]], [0.1, v[2] + 0.1], "g", linewidth=3)
ax.plot([0, w[0]], [0, w[1]], [0, w[2]], "b")

# now draw plane
xx, yy = np.meshgrid(range(-15, 16), range(-15, 16))
cp = np.cross(S1, S2)
z1 = (-cp[0] * xx - cp[1] * yy) * 1.0 / cp[2]
ax.plot_surface(xx, yy, z1)

plt.show()
