# 1-е задание
class Matrix:
    matrix = []

    def __init__(self, l):
        self.matrix = l

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += f'|{" ".join(map(str, row))}|\n'
        return result

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return 'Матрицы разных размеров. Сложение невозможно'

        new = []
        for i in range(len(self.matrix)):
            new.append(map(sum, zip(self.matrix[i], other.matrix[i])))

        return Matrix(new)


m = Matrix([[1, 2, 3], [4, 5, 6]])

print(m)

m2 = Matrix([[9, 8, 7], [6, 5, 4]])
print(m2 + m)
