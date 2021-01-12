# 5-е задание
stop = True
l_sum = 0
while stop:
    l = input('Введите набор цифр. Для остановки ввода, введите значение Y: ').split()
    for value in l:
        try:
            l_sum += float(value)
        except ValueError:
            if value == 'Y':
                stop = False
                break

    print(f'сумма чисел = {l_sum}')

