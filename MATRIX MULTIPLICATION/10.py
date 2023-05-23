# ELEMENT-WISE (HADAMARD) MULTIPLICATION

import numpy as np

# any matrix sizes
m = 13
n = 2

# ...but the two matrices must be the same size
A = np.random.randn(m, n)
B = np.random.randn(m, n)

# In python, asterisk(*) means element-wise multiplication
C1 = np.multiply(A, B)
C2 = A * B

print(C1), print(" ")
print(C2), print(" ")

print(C1 - C2)
