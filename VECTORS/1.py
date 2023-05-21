# Algebraic and Geometric Interpretations of Vectors

import numpy as np
import matplotlib.pyplot as plt

# 2-dimensional vector
v2 = [3, -2]

# 3-dimensional vector
v3 = [4, -3, 2]

# The vectors above are row vectors. By transposing, you get column vectors
v3_transposed = np.transpose(v3)


# Plotting 2D vector (starting from the origin)
def plot_2D(vector, start=[0, 0]):
    if start[0] == 0 and start[1] == 0:
        plt.plot([0, v2[0]], [0, v2[1]])
        plt.axis("equal")
        plt.plot([-4, 4], [0, 0], "k--")
        plt.plot([0, 0], [-4, 4], "k--")
        plt.grid()
        plt.axis((-4, 4, -4, 4))
        plt.show()
    else:
        plt.plot([start[0], v2[0]], [start[1], v2[1]])
        plt.axis("equal")
        plt.plot([-4, 4], [0, 0], "k--")
        plt.plot([0, 0], [-4, 4], "k--")
        plt.grid()
        plt.axis((-4, 4, -4, 4))
        plt.show()

if __name__ == '__main__':
    vector = [3, -2]
    plot_2D(vector)
