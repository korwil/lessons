# 3-е задание
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


a = Position('Иван', 'Иванов', 'Инженер', 22000, 15000)
print(f'Полное имя: {a.get_full_name()}, должность: {a.position}, доход: {a.get_total_income()}')
