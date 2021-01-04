# 6-е задание
from itertools import count
from sys import argv

try:
    a = int(argv[1])
except:
    a = int(input('Введите число: '))

for el in count(a):
    if el > a + 10:
        break
    else:
        print(el)
