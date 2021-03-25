# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json

l_result = []
profit = {}
prof_aver = 0
with open('file7.txt', 'r', encoding='UTF-8') as file:
    i = 0
    pr = 0
    for line in file:
        name, _, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit[name] >= 0:
            pr += profit[name]
            i += 1
    l_result.append(profit)
    if i > 0:
        pr = round(pr/i)

    l_result.append({'average_profit': pr})

with open('file7.json', 'w') as write_js:
    json.dump(l_result, write_js)
