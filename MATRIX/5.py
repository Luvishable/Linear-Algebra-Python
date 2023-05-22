# DIAGONAL AND TRACE

import numpy as np

M = np.round(5 * np.random.randn(4, 4))

# extract the diagonals
diagonal = np.diag(M)

# NOTE: diag function has two ways to use. First, it extracts the diagonal from a matrix; second it creates a matrix from
# a diagonal.
d = np.diag(M)  # input is matrix, output is vector
D = np.diag(d)  # input is vector, output is matrix
print(d)
print(D)

# trace is the sum of diagonal elements. Trace is only defined for square matrices!!!
trace1 = np.trace(M)  # first method
trace2 = sum(np.diag(M))
print(trace1, trace2)
