from Mandas import Matrix
import numpy as np

def dot(a, b):
    if isinstance(a, Matrix):
        a = a.matrix
    if isinstance(b, Matrix):
        b = b.matrix
    return np.dot(a, b)