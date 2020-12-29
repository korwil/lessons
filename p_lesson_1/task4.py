# 4-е задание
a = int(input('Введите число: '))
maximus = 0
while a > 0 or maximus == 9:
    tmp = a % 10
    if maximus < tmp:
        maximus = tmp
    a = a // 10

print(f'Максимальное число: {maximus}')




