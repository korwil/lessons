# 4-е задание
def my_func(x, y):
    return x ** y


# Альтернатива
def my_func2(a, n):
    if a == 0:
        return 0
    b = 1
    while n < 0:
        n += 1
        b *= a
    return 1 / b


print(f'Произведение = {my_func(2.1, -3)}')
print(f'Произведение = {my_func2(3.1, -3)}')
