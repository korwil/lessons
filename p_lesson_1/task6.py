# 6-е задание
km = int(input('За первый день: '))
result = int(input('Результат, который хотим достич: '))
day = 1

if result > km > 0:
    while km < result:
        print(f'{day}-й день: {km:.2f}')
        km += km/10
        day += 1

    print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {result} км. А точнее: {km:.2f}')

elif km >= result:
    print('Вы уже лучший')

else:
    print('Безнадежно')



