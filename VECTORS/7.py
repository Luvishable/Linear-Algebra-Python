# Dot Product Geometry: Sign and Orthogonality

import numpy as np
import matplotlib.pyplot as plt

# To find the angle between two vectors:
# 1) Take the dot product of two vectors
# 2) Divide the result with the multiplication of the lengths of the vectors
# 3) Find the arccos value

# NOTE: np.linalg.norm() is for finding the length of the vector
# NOTE: Actually, algebraic and geometric dot product formulas are equiavalent


def geometric_dot_product(vector1, vector2, plot=True):
    angle = np.arccos(
        np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    )
    dot_product_geometric = (
        np.linalg.norm(vector1) * np.linalg.norm(vector2) * np.cos(angle)
    )
    if plot == True:
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        ax.plot([0, vector1[0]], [0, vector1[1]], [0, vector1[2]], "b")
        ax.plot([0, vector2[0]], [0, vector2[1]], [0, vector2[2]], "r")

        plt.axis((-6, 6, -6, 6))
        plt.title("Angle between vectors: %s rad." % angle)
        plt.show()
    return dot_product_geometric


if __name__ == "__main__":
    v1 = np.array([2, 4, -3])
    v2 = np.array([0, -3, -3])
    print(geometric_dot_product(v1, v2, plot=True))
