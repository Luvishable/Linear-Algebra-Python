import numpy as np

# There are four ways to consider matrix multiplication: element-wise, layer perspective, column perspective and
# row perspective

# Let's implement matrix multip. via layer perspective

# generate two matrices
m = 4
n = 6

A = np.random.randn(m, n)
B = np.random.randn(n, m)

# build the product matrix layer-wise
C1 = np.zeros((m, m))  # AxB => 4x6 x 6x4 => 4x4 (this is why C1 is 4x4 matrix)
for i in range(n):
    C1 += np.outer(A[:, i], B[i, :])

# Implement matrix multiplication
C2 = A @ B

# compare the results
print(np.round(C1, 2))
print(np.round(C2, 2))
print(np.round(C1, 2) == np.round(C2, 2))
