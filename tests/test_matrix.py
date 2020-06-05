from Mandas import Matrix
import numpy as np

def test_pop():
    T = Matrix([[1,2,3], [4,5,6], [7,8,9]])
    T.pop(3)
    assert(np.sum(T.matrix == np.array([[1,2], [4,5]])) == 4)