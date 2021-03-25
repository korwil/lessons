# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

amount = 0
with open('file3.txt', 'r', encoding='UTF-8') as file:
    personnel = file.readlines()

person_20 = []
for person in personnel:
    tmp = person.replace('\n', '').split()
    salary = int(tmp[1])
    amount += salary
    if salary < 20000:
        person_20.append(tmp[0])

print(f'Средняя зарплата = {amount/len(personnel)}')
print('Менее 20 тыс. получают:', *person_20, sep='\n')







