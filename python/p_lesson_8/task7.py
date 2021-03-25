# 7-е задание

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.number = complex(a, b)

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        # z = z1⋅z2 = (a1a2−b1b2) + (a1b2 + b1a2)i
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        return f'Число: {self.number}'


z1 = Complex(1, 2)
z2 = Complex(3, 4)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)

print('======')
print(z1.number + z2.number)
print(z1.number * z2.number)
