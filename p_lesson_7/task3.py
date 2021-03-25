# 3-е задание
class Cell:

    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __str__(self):
        return f'Количество ячеек в клетке = {self.nucleus}'

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus < other.nucleus:
            return 'разность количества ячеек двух клеток меньше нуля'
        return Cell(self.nucleus - other.nucleus)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        try:
            return Cell(self.nucleus // other.nucleus)
        except ZeroDivisionError:
            return 'Деление на ноль'

    def make_order(self, n):
        if n == 0:
            results = 'Некорректное значение'
        else:
            results = ''
            for x in range(self.nucleus//n):
                results += f'{"*" * n}\n'
            results += f'{"*" * (self.nucleus % n)}'

            # Альтернатива:
            # results = ''.join(['*\n' if x % n == 0 else '*' for x in range(1, self.nucleus + 1)])
        return results


c1 = Cell(12)
c2 = Cell(3)

print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1/c2)
print(c1.make_order(5))




