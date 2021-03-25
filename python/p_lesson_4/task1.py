# 1-е задание
from sys import argv

if len(argv) < 4:
    print('Введены не все параметры')
else:
    print(f'Заработная плата = {(float(argv[1])*float(argv[2])) + float(argv[3])}')





