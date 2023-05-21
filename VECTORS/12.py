# Hermitian Transpose

import numpy as np

# Sometimes called Conjugate Transpose or Complex Conjugate Transpose
# Hermitian Transpose is necessary for vectors that contain complex numbers

# Complex Number => Complex Conjugate:
# change the sign of the imaginary part. By doing so, we flip the complex number across real axis.

# Conjugate transposed indicated as H or asterisk(*) instead of T which means normal transpose

# create a complex number
z = complex(3, 4)

# magnitude
magnitude = np.linalg.norm(z)

# np.transpose does not implement hermitian transpose so first we have to conjugate the complex number
hermitian_transposed = np.transpose(z.conjugate()) * z

print(f"Hermitian Transposed Vector is {hermitian_transposed}")
print()

# complex vector
v = np.array([3, 4j, 5 + 2j, complex(2, -5)])
print(f"Complex vector is {v}")
print()
print(f"Hermitian Transposed vector is {np.transpose(v.conjugate())}")
