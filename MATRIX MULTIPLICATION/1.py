# STANDARD MATRIX MULTIPLICATION

import numpy as np

# Matrix multip. is not commutative(AxB does not equal to BxA)

# Matrix multip. is valid only when the inner dimensions match and the size of the product matrix corresponds to the size
# of the outer dimensions.

m = 4
n = 3
k = 6

# make some matrices
A = np.random.randn(m, n)
B = np.random.randn(n, k)
C = np.random.randn(m, k)

# np.matmul(A, B) # 4x3 x 3x6 => 4x6 (VALID)
# np.matmul(A, A) # 4x3 x 4x3 => ERROR (NOT VALID: inner dimensions do not match)
# np.matmul(A.T, C) 3x4 x 4x6 => 3x6 (VALID)
# np.matmul(B, B.T) 3x6 x 6x3 => 3x3 (VALID)
# np.matmul(np.matrix.transpose(B), B) 6x3 x 3x6 => 6x6 (VALID)
# np.matmul(B, C) 3x6 x 4x6 => ERROR (NOT VALID: inner dimensions do not match)
# np.matmul(C, B) 4x6 x 3x6 => ERROR (NOT VALID: inner dimensions do not match)
# np.matmul(C.T, B) 6x4 x 3x6 => ERROR (NOT VALID: inner dimensions do not match)
# np.matmul(C, B.T) 4x6 x 6x3 => (VALID)
