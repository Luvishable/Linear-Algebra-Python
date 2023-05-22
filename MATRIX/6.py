# THE LINEARITY OF TRACE

import numpy as np

# We are gonna explore whether or not:      trace(A) + trace(B) == trace(A+B)
#                                           trace(l * A) == l * trace(A)
# If trace is a linear operator, then the quantities above should be equal.

m = 4
n = 4

A = np.random.randn(m, n)
B = np.random.randn(m, n)

l = np.random.randn()

print("trace(A + B) = " + str(np.trace(A + B)))
print("trace(A) + trace(B) = " + str(np.trace(A) + np.trace(B)))
print("-----------------------------------------------")
print("trace(l * A) = " + str(np.trace(l * A)))
print("l * trace(A) = " + str(l * np.trace(A)))

# As can be seen from the outputs, the trace is a linear operator.
