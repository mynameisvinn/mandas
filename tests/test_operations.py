from Mandas import Matrix, dot
import numpy as np

def test_dot():
    T = Matrix(np.array([[1,2,3], [4,5,6], [7,8,9]]))
    U = Matrix(np.array([[1,2,3], [4,5,6], [7,8,9]]))
    assert(np.sum(dot(T, U) == np.array([[ 30,  36,  42], [ 66,  81,  96], [102, 126, 150]])) == 9)