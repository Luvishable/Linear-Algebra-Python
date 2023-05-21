# Length of a Vector

import numpy as np
from math import sqrt

# Sometimes a length of vector can be called 'magnitude of a vector' or 'norm of a vector'.

# To find the length of a vector, you just take the root of the dot product of the vector itself

def find_length_2D(vector):
     length = sqrt(sum(np.multiply(vector, vector)))
     return length

if __name__ == '__main__':
    vector = np.array([1,2,3,4,5,7])
    print(find_length_2D(vector))