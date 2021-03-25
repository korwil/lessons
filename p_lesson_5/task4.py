# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
lines = []

with open('file4.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        tmp = line.split(' ', 1)
        lines.append(my_dict[tmp[0]] + ' ' + tmp[1])

with open('new_file4.txt', 'w', encoding='UTF-8') as file:
    file.writelines(lines)






