value_l = ['название', 'цена', 'количество', 'единица измерения']
l = []
n = 'y'
i = 0
while n == 'y':
    d = {}
    i += 1
    for value in value_l:
        d[value] = input(f'Введите {value}: ')
    l.append((i, d))
    n = input('Для ввода еще одного элемента в список, нажмите y: ').lower()
print(f'Введен список: {l}')
d = {}

for value in value_l:
    tmp = set()
    for tup in l:
        tmp.add(tup[1][value])
    d[value] = list(tmp)

print(d)


