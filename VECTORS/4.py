# Vector-Vector Multiplication: Dot Product

import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1, 2, 3, 4, 5, 6])
v2 = np.array([0, -4, -3, 6, 5])

# First Method: The most verbose way to calculate the dot product is following
dot_product1 = 0
for i in range(len(v1)):
    dot_product1 += v1[i] * v2[i]

# We can utilize different methods in numpy in order to find the dot product of two vectors

# Second Method:
dot_product2 = sum(np.multiply(v1, v2))

# Third Method:
dot_product_3 = np.dot(v1, v2)

# Fourth Method:
dot_product4 = np.matmul(v1, v2)

# NOTES:
# 1) Since dot product is a single number, it is sometimes called scalar product
# 2) If we wanna find a dot product of two vectors, the vectors have to be same dimensionality
# 3) Dot product is generally written as: (transposed of first vector * second vector)
# 4) Dot product will be always a single number regardless of dimension