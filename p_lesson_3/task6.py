# 6-е задание

def int_func(text):
    return text.capitalize()


print(int_func('text'))

l = input('Введите слова через пробел: ').split()

for value in l:
    print(int_func(value), end=' ')
