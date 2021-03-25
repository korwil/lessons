# 1-е задание
a = float(input('Введите числитель: '))
b = float(input('Введите знаменатель: '))


def division(x, y):
    if y == 0:
        return None
    return x / y


# Альтернатива
def division2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None


print(f'a / b = {division(a, b)}')
print(f'a / b = {division2(a, b)}')
