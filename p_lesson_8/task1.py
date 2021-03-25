# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

MONTH_DATE = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        try:
            l = [int(i) for i in date.split('-')]
        except:
            raise Exception('Неверный формат')
        return l

    @staticmethod
    def validation(number=None, month=None, year=None):
        if year is not None:
            if type(year) != int:
                raise Exception('Год в неверном формате')
            elif year >= 0:
                print(f'год {year}')
            else:
                print(f'Сейчас {year * -1} до н.э.')

        if month is not None:
            if type(month) != int:
                raise Exception('Неверный формат месяца')
            elif 1 > month >= 12:
                raise Exception('Месяц меньше 1 или больше 12')
            else:
                print('месяц — от 1 до 12')

        if number is not None:
            if type(number) != int:
                raise Exception('Число в неверном формате')
            elif year and month and year % 4 == 0 and month == 2 and 29 >= number > 0:
                print(f'Число для месяца 02(Февраль) и года {year} - верное')
            elif month is not None and month in MONTH_DATE and MONTH_DATE[month] >= number > 0:
                print(f'Число для месяца {month} - верное')
            elif 31 >= number > 0 and month is None:
                print('Число верное')
            else:
                raise Exception('Число неверно')
        else:
            raise Exception('Число некорректного формата')


d = Date('08-12-1202')
n, m, y = Date.get_date('02-02-2020')
print(f' Число = {n}, Месяц = {m}, Год = {y}')
d.validation(number=30)
# Date.validation(number=29, month=2, year=2021)
Date.validation(number=29, month=2, year=2020)
