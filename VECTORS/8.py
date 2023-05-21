# The Cauchy - Schwarz Inequality

import numpy as np

# The Cauchy-Schwarz Inequality says that the absolute value or the magnitude of the dot product between two vectors
# is less than or equal to the multiplication of the norms of those two vectors.

# create three vectors, one of which is dependent on another
a = np.random.randn(5)
b = np.random.randn(5)
c = np.random.randn(1) * a

# compute their products
aTb = np.dot(a, b)
aTc = np.dot(a, c)

# demonstrate the (in)equalities
print(f"{np.abs(aTb):.4f}, {np.linalg.norm(a) * np.linalg.norm(b):.4f}")
print(f"{np.abs(aTc):.4f}, {np.linalg.norm(a) * np.linalg.norm(c):.4f}")

# Since the a and c vectors are linearly dependent on each other, the cosine value of the angle between these vectors
# will be 0 and cos0 = 1. But in other situations where the cos is between 0-1 the dot product will be multiplied by a
# number less than 1 (above 0 because we take abs of it) and the result will be less than the multiplications of the
# norms of the vectors.

# NOTE: If the dot products of two vectors is 0, they are orthogonal to each other.
