from copy import deepcopy


class Matrix:
    def __init__(self, matrix: list):
        # validate matrix
        for row in matrix:
            if len(row) != len(matrix):
                raise ValueError('Invalid matrix')

        self.__matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join([str(number) for number in row]) for row in self.__matrix])

    def __add__(self, new):
        result = deepcopy(self.matrix)

        for row_index, row in enumerate(result):
            for number_index, number in enumerate(row):
                result[row_index][number_index] += new.matrix[row_index][number_index]

        return Matrix(result)

    @property
    def matrix(self):
        return self.__matrix


matrix1 = Matrix([
    [1, 6, 8],
    [4, 7, 3],
    [5, 2, 7],
])

matrix2 = Matrix([
    [4, 2, 1],
    [8, 5, 6],
    [5, 3, 9],
])

print(matrix1)
print()
print(matrix2)
print()
print(matrix1 + matrix2)
