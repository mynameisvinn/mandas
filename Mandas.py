from sklearn.base import BaseEstimator
import numpy as np

class Matrix(BaseEstimator):
    def __init__(self, matrix):
        self.matrix = matrix
        self.labels = self.create_labels(matrix)
        
    def create_labels(self, matrix):
        """
        k = matrix label, v = corresponding list position
        """
        labels = {}  
        for i in range(len(matrix[0])):
            labels[i + 1] = i
        return labels
        
    def pop(self, p):
        """remove row/col index from matrix.
        """
        if p not in self.labels.keys():
            raise Exception("row does not exist")
        
        # step 1: remove key from labels
        skip = self.labels[p]
        self.labels.pop(p)

        
        # step 2: update index position for everything that follows
        for k, v in self.labels.items():
            if k > p:
                self.labels[k] -= 1
        
        # step 3: recreate matrix with updated rows
        # https://stackoverflow.com/questions/10996140/how-to-remove-specific-elements-in-a-numpy-array
        self.matrix = np.array([list(np.delete(row, skip)) for i, row in enumerate(self.matrix) if i!= skip])
        return self.matrix
                