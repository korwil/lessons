# 3-е задание
def my_func(x, y, z):
    l = [x, y, z]
    l.sort()

    return sum(l[-2:])


# Альтернатива
def my_func2(*args):
    return sum(sorted(args)[-2:])


a = float(input('Введите 1=е число: '))
b = float(input('Введите 2=е число: '))
c = float(input('Введите 3=е число: '))

print(f'Сумма наибольших чисел = {my_func(a, b, c)}')
print(f'Сумма наибольших чисел = {my_func2(a, b, c)}')

