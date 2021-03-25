# 2-e задание
time = int(input('Введите количество секунд: '))
print(f'Введено секунд: {time}')

sec = time % 60
minutes = time // 60 % 60
hours = time // 60 // 60

print(f'Время в формате чч:мм:сс: {hours:02d}:{minutes:02d}:{sec:02d}')



