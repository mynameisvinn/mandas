from Mandas import Matrix
import numpy as np

def dot(a, b):
    if isinstance(a, Matrix):
        a = a.matrix
    if isinstance(b, Matrix):
        b = b.matrix
    return np.dot(a, b)

def is_acyclic(m):
    k = len(m)  # number of vertices in adjacency matrix
    for _ in range(k):
        m = dot(m, m)
    return np.sum(m) == 0