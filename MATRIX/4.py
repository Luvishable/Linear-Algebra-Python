# TRANSPOSE

import numpy as np

# create a matrix
M = np.array([[1, 2, 4], [6, 3, 5]])

# tranpose (short way)
print(M.T), print("---------------------------------")

# transpose via numpy
print(np.transpose(M)), print("---------------------------------")

# In python, the transpose is not the Hermitian Transpose as you saw before in Vectors. So if you want to transpose
# a matrix, first you have to call conjugate method on the matrix and then transpose it.

# create a complex valued matrix
C = np.array([[4 + 1j, 3, 2 - 4j]])

hermitian_transposed = C.conjugate().T
print(hermitian_transposed)
