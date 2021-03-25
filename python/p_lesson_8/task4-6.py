# 3-е задание
A1 = 'A1'
A2 = 'A2'
A3 = 'A3'
A4 = 'A4'
ALL_FORMATS = [A1, A2, A3, A4]


class NotExistInWarehouse(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'На складе нет {self.name}'


def exist_in_warehouse(dict):
    def dec_exist(func):
        def wrap_exist(cls, department, name, count):
            if name not in dict:
                raise NotExistInWarehouse(name)
            return func(cls, department, name, count)

        return wrap_exist

    return dec_exist


class Warehouse:
    dict_kept = {}
    dict_not_kept = {}

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'На слкаде: {self.dict_kept}. В депортаментах: {self.dict_not_kept}'

    def add_equipment(self, equipment, count):
        all = sum(self.dict_kept.values())
        if self.size >= all + count:
            self.dict_kept = self.__check_and_add(self.dict_kept, equipment.name, count)
        elif all + count > self.size > all:
            r = input(f'На складе можно разместить только: {self.size - all} едениц. Согласны? Y/N ')
            if r.lower() == 'y':
                self.dict_kept[equipment.name] = self.size - all
        else:
            print('Склад полон')

    @exist_in_warehouse(dict_kept)
    def sent_to_department(self, department, name, count):
        if count <= self.dict_kept[name]:
            # Можно еще добавить проверок, но хватит
            self.dict_not_kept[department] = {
                name: count
            }
            self.dict_kept[name] -= count
        else:
            print(f'На складе нет такого количества')

    @staticmethod
    def __check_and_add(dict, name, count):
        if name in dict:
            dict[name] = dict[name] + count
        else:
            dict[name] = count
        return dict



class officeEquipment:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        try:
            self.__cost = float(cost)
        except ValueError:
            print('Цена в неверном формате')


class Scan(officeEquipment):
    def __init__(self, name, cost, format):
        self.format = format
        super().__init__(name, cost)

    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format):
        if type(format) == str and format in ALL_FORMATS:
            self.__format = [format]
        elif type(format) == list and all(i in ALL_FORMATS for i in format):
            self.__format = format
        else:
            print(f'Неверное значение формата {format}')


class Print(officeEquipment):
    def __init__(self, name, cost, format, color=False):
        self.format = format
        self.color = color
        super().__init__(name, cost)

    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format):
        if type(format) == str and format in ALL_FORMATS:
            self.__format = [format]
        elif type(format) == list and all(i in ALL_FORMATS for i in format):
            self.__format = format
        else:
            print(f'Неверное значение формата {format}')


class Xerox(officeEquipment):
    def __init__(self, name, cost, color=False):
        self.color = color
        super().__init__(name, cost)


xer = Xerox('Xerox XP', 2000.00)
prin = Print('Canon', 3500, [A1, A3], True)
scan = Scan('Hp', '1200', [A2, A4])

war = Warehouse('Склад1', 15)

war.add_equipment(xer, 5)
print(war)

war.add_equipment(prin, 13)
war.add_equipment(scan, 2)
print(war)

war.sent_to_department('Dev', prin.name, 2)
print(war)

war.sent_to_department('Dev', 'Scan', 2)
