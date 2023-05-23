# MATRIX-VECTOR MULTIPLICATION

import numpy as np

# number of elements
m = 4

# create matrices
N = np.random.randint(-10, 11, (m, m))
S = np.round(N.T * N / m**2)  # scaled symmetric

# vector
w = np.array([-1, 0, 1, 2])

# with symmetric matrix
print(S @ w)  # 1
print(S.T @ w)  # 2
print(w @ S)  # 3
print(w.T @ S.T)  # 4
print(w.T @ S)  # 5

print("-------------------------------------------------------")

# with nonsymmetric matrix
print(N @ w)  # 1
print(N.T @ w)  # 2
print(w @ N)  # 3
print(w.T @ N.T)  # 4
print(w.T @ N)  # 5

# EXPLANATION
# let S = symmetric matrix     w = vector
# (S @ w) == (S.T @ w) == (w @ S) == (w.T @ S.T) == (w.T @ S)
