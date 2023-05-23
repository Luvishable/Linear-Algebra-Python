# Based on the 5.py, we are gonna study the pure and impure transformation matrices

import math
import numpy as np
import matplotlib.pyplot as plt

# The result of transformation matrix multiply by vector does not change the length of the input vector; it just
# rotates it while maintaining its length.

thetas = np.linspace(0, 2 * np.pi, 100)

vecmags = np.zeros((len(thetas), 2))  # vector magnitudes
v = np.array([-1, 2])
for i in range(len(thetas)):
    th = thetas[i]
    A1 = np.array([[2 * math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
    A2 = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])

    # compute vector magnitudes
    vecmags[i, 0] = np.linalg.norm(A1 @ v.T)
    vecmags[i, 1] = np.linalg.norm(A2 @ v.T)

# plt.plot(thetas, vecmags, "-")
# plt.xlabel("Rotation Angle (rad.)")
# plt.ylabel("Average Magnitude")
# plt.legend(["pure rotation", "impure rotation"])
# plt.show()



