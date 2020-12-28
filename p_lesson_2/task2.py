l = []
n = 'y'
while n == 'y':
    l.append(input('Введите значение в список: '))
    n = input('Для ввода еще одного элемента в список, нажмите Y: ').lower()
print(f'Введен список: {l}')

result = []
for i in range(0, len(l), 2):
    tmp = l[i:i+2]
    result += tmp[::-1]

print(result)




