# 6-е задание
from itertools import cycle

a = [1, 'da', None]
i = 0
for el in cycle(a):
    if i == 3*len(a):
        break
    print(el)
    i += 1
