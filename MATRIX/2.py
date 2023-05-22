# MATRIX ADDITION AND SUBTRACTION

import numpy as np

# create random matrices
A = np.random.randn(5, 4)
B = np.random.randn(5, 3)
C = np.random.randn(5, 4)

# Add them
A_B = A + B
A_C = A + C

# shifting a matrix
lambda_ = 0.3
N = 5  # the size of square matrix
D = np.random.randn(N, N)

D_shifted = D + lambda_ * np.eye(N)

# NOTE: Shifting a matrix does not change off-diagonal elements. It changes diagonal elements.
