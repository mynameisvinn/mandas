import numpy as np

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.labels = self.create_labels(matrix)
        
    def __repr__(self):
        return str(self.matrix)
    
    def __len__(self):
        return len(self.matrix) ** 2
        
    def create_labels(self, matrix):
        """create a dictionary where k = user label, v = corresponding list position.
        
        labels are modified whenever the adjacency matrix is modified.
        """
        labels = {}  
        for i in range(len(matrix[0])):
            labels[i + 1] = i
        return labels
        
    def pop(self, p):
        """remove row/col index from matrix.
        """
        if p not in self.labels.keys():
            raise Exception("vertex does not exist")
        
        # step 1: remove key from labels
        skip = self.labels[p]  # skip is the index representing vertex to be popped
        self.labels.pop(p)

        # step 2: shift index positions for subsequent vertices
        for k, v in self.labels.items():
            if k > p:
                self.labels[k] -= 1
        
        # step 3: recreate matrix by skipping the appropriate row and column
        # https://stackoverflow.com/questions/10996140/how-to-remove-specific-elements-in-a-numpy-array
        self.matrix = np.array([list(np.delete(row, skip)) for i, row in enumerate(self.matrix) if i!= skip])
        return self.matrix
                