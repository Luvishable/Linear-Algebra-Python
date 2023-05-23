# ADDITIVE AND MULTIPLICATIVE SYMMETRIC MATRICES

import numpy as np

## ADDITIVE METHOD

# specify sizes
m = 5
n = 5

# create matrices
A = np.random.randn(m, n)
S = (A + A.T) / 2

# A symmetric matrix minus its transpose equals zeros
print(S - S.T)

## MULTIPLICATIVE METHOD

# specify sizes
m = 5
n = 3

# create matrices
A = np.random.randn(m, n)
AtA = A.T @ A
AAt = A @ A.T

# first, show that they are square
print(AtA.shape)
print(AAt.shape)

# next, show that they are symmetric
print(AtA - AtA.T)
print(AAt - AAt.T)
