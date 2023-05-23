# ORDER OF OPERATIONS ON MATRICES

import numpy as np

n = 2

L = np.random.randn(n, n)
I = np.random.randn(n, n)
V = np.random.randn(n, n)
E = np.random.randn(n, n)

# result of forward multiplication and then transpose
result1 = np.matrix.transpose(L @ I @ V @ E)

# result of flipped multiplication of transposed matrices
result2 = E.T @ V.T @ I.T @ L.T

# check if they are equal
print(result1 == result2)
