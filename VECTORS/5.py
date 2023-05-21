# Dot Product Properties: Associative, Distributive, Commutative

import numpy as np
import matplotlib.pyplot as plt

# Distributive:
#   a(b + c) = a.b + a.c

# Associative:
#   a.(b.c) = (a.b).c

# The dot product is distributive but not associative

# Creating random vectors by utizing np.random.randn. This function creates an array of specified shape and fills it
# with random values as per standard distribution
n = 10
v1 = np.random.randn(n)
v2 = np.random.randn(n)
v3 = np.random.randn(n)

# Let's prove that dot product is distributive
result1 = np.dot(v1, (v2 + v3))
result2 = np.dot(v1, v2) + np.dot(v1, v3)
# NOTE: Since the results are float numbers, we better round the results.
print(
    f"Dot product is distributive since the result is {result1.round(4) == result2.round(4)}"
)

# Now, let's prove that dot product is not associative.
result3 = np.dot(v1, np.dot(v2, v3))
result4 = np.dot(np.dot(v1, v2), v3)
print(
    f"Dot product is not associative since the result is {result3.round(4) == result4.round(4)}"
)

# Dot product is commutative. Let's prove:
# What is commutative? => a*b == b*a

# Generating two 100-element vectors
a = np.random.randn(100)
b = np.random.randn(100)

# compute the dot products of a.b and b.a
dp_ab = np.dot(a, b)
dp_ba = np.dot(b, a)

# We can say that the subtraction of the dot products have to be 0 since they are equal.
print(dp_ab, "\n", dp_ba, "\n", dp_ab - dp_ba)
