#  Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
#  количества слов в каждой строке.
try:
    with open('file2.txt', 'r', encoding='UTF-8') as file:
        count = 0
        for line in file:
            count += 1
            print(f'Количество слов в строке №{count}: {len(line.split())}')

        print(f'Общее число строк: {count}')
except IOError:
    print('Произошла ошибка чтения файла')
