# 2-e задание

def my_func(**kwargs):
    print(f'Меня зовут {kwargs["name"]} {kwargs["l_name"]}, '
          f'мне {kwargs["age"]}. '
          f'Живу в городе - {kwargs["city"]}. '
          f'Мои контакты: {kwargs["phone"]}, {kwargs["email"]}')


my_func(name='Иван', l_name='Иванов', age=22, city='Москва', email='test@test.ru', phone='+79999999999')




