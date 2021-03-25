l = input('Введите строку из нескольких слов, разделённых пробелами: ').split()

for i, value in enumerate(l):
    i += 1
    print(f'{i}: {value[:10]}')
