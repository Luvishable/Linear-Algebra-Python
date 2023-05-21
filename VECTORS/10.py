# Outer Product

import numpy as np

# Outer product is generally written as (first vector * transposed of second vector)
# Outer product, in contrast to dot product, is not a single number, nut instead a matrix.
# Unlike the dot product, outer product can be computed between two vectors that do not have the same dimensionality

# Outer product: the column perspective:
# |1| * |a b c d|       |1a 1b 1c 1d|
# |0|               =   |0a 0b 0c 0d|
# |2|                   |2a 2b 2c 2d|
# |5|                   |5a 5b 5c 5d|

v1 = np.array([1, 2, 3])
v2 = np.array([-1, 0, 1])

# outer product
outer_product = np.outer(v1, v2)

# or manually:
outer_product_manually = np.zeros((len(v1), len(v2)))
for i in range(len(v1)):
    for j in range(len(v2)):
        outer_product_manually[i, j] = v1[i] * v2[j]

if __name__ == "__main__":
    print(outer_product_manually)
