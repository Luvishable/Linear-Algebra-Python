# BROADCASTING MATRIX ARITHMETIC

import numpy as np

# create a matrix
A = np.reshape(np.arange(1, 13), (3, 4), "F")  # F=column C=row

# create two vectors(they are row vectors default)
r = [10, 20, 30, 40]
c = [100, 200, 300]

# In Python, we are allowed to broadcast on the rows but not on columns.
print(A + r)

# If you want to broadcast on the columns, you have to convert the row vector into column vector explicitly
print(A + np.reshape(c, (len(c), 1)))
