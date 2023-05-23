# STANDARD AND HADAMARD MULTIPLICATION FOR DIAGONAL MATRICES

import numpy as np

# create two square matrices: 'full' and 'diagonal'
A = np.random.randn(4, 4)
D = np.diag(np.random.randn(4))

# multiply each matrix by itself: Standard and Hadamard
print(A @ A), print(" ")
print(A * A), print(" ")

print(D @ D), print(" ")
print(D * D), print(" ")

# As can be seen, diagonal square matrices produces the same result whether it is standard multiplication or hadamard
