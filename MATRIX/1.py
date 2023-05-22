# MATRIX TYPES

import numpy as np


def create_matrix(type):
    if type == "square":
        S = np.random.randn(5, 5)
        return S
    elif type == "rectangular":
        R = np.random.randn(5, 2)
        return R
    elif type == "identity":
        I = np.eye(3)
        return I
    elif type == "zeros":
        Z = np.zeros((4, 4))
        return Z
    elif type == "diagonal":
        D = np.diag([1, 2, 3, 5, 2])
        return D
    elif type == "triu":
        S = np.random.randn(5, 5)
        U = np.triu(S)
        return U
    elif type == "tril":
        S = np.random.randn(5, 5)
        U = np.tril(S)
        return U
