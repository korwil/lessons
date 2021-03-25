# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

def get_digit(num):
    tmp = 0
    if num.isdigit():
        tmp = int(num)

    return tmp


my_dict = {}
with open('file6.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        my_dict[subject] = get_digit(lecture) + get_digit(practice) + get_digit(lab)

print(my_dict)


