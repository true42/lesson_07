import numpy as np


class Matrix:
    def __init__(self, list_matrix):
        self.list_matrix = np.array(list_matrix)

    def __str__(self):
        return np.array_str(self.list_matrix)

    def __len__(self):
        return self.list_matrix.size

    def __add__(self, add_matrix):
        if self.list_matrix.size == add_matrix.list_matrix.size and self.list_matrix[0].size == add_matrix.list_matrix[0].size:
            x = self.list_matrix + add_matrix.list_matrix
            return x
        else:
            return f'Сложить можно только одинаковые по размеру матрицы'


x = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
y = Matrix([[3, 2, 1], [3, 2, 1], [3, 2, 1]])

a = x+y
print(a)
