# SYMMETRY OF COMBINED SYMMETRIC MATRICES

import numpy as np

# create two symmetric matrices
m = 3

A = np.random.randn(m, m)
AtA = A.T @ A

B = np.random.randn(m, m)
BtB = B.T @ B

# compute sum, multiplication and Haadamard multiplication
Cs = AtA + BtB  # sum
Cm = AtA @ BtB  # multiplication
Ch = AtA * BtB  # Haadamard

# determine whether result is symmetric
print(Cs - Cs.T), print(" ")
print(Cm - Cm.T), print(" ")
print(Ch - Ch.T)

# NOTE: In order to create a symmetric matrix, M x M.T
