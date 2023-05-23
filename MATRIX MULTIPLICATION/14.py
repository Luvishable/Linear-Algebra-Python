# FROBENIUS DOT PRODUCT

import numpy as np

# any matrix sizes
m = 9
n = 4

# but the two matrices must be the same size
A = np.random.randn(m, n)
B = np.random.randn(m, n)

# first vectorize, then vector-dot-product
Av = np.reshape(A, m * n, order="F")  # order='F' reshapes by columns instead of by rows
Bv = np.reshape(B, m * n, order="F")
frob_dp = np.dot(Av, Bv)

# trace method
frob_dp2 = np.trace(A.T @ B)
print(frob_dp2)
print(frob_dp)

# matrix norm
Anorm = np.linalg.norm(A, "fro")
Anorm2 = np.sqrt(np.trace(A.T @ A))
# print(Anorm)
# print(Anorm2)

# The second approach(trace) is more clear. We just transpose first matrix and then multiply it by second matrix. Then
# sum the elements in the diagonal which is called trace.