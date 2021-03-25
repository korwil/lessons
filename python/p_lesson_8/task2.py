# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'Ошибка: {self.txt}'


numerator = input('Введите числитель: ')
denominator = input('Введите знаменатель: ')

try:
    n = int(numerator)
    d = int(denominator)
    if d == 0:
        raise ZeroDivision('Поделили на ноль')
except ValueError:
    print("Вы ввели не число")
except ZeroDivision as err:
    print(err)
else:
    print(n/d)
