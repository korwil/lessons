# 1-е задание
print('Первое задание')
array = {
    'str': 'str',
    'int': 123,
    'tuple': (1, 2, 3)
}

print(array['tuple'])
print(type(array['tuple']))

value_str = input('Введите строку: ')
value_int = int(input('Введите целое число: '))
value_bool = bool(int(input('Введите 1/0 ')))
print(f'Введено значение {value_str} с типом {type(value_str)}')
print(f'Введено значение {value_int} с типом {type(value_int)}')
print(f'Введено значение {value_bool} с типом {type(value_bool)}')




