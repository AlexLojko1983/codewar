def determinant(matrix):
    import numpy as np
    return (round(np.linalg.det(matrix)))
matrix = [[1,2,3],[4,5,8],[8,5,9]]
print(determinant(matrix))