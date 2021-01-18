# 4-е задание
import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        return 'поехала'

    @staticmethod
    def stop():
        # self.speed = 0 - раз остановилась, нужно ли скорость сбросить?
        return 'остановилась'

    @staticmethod
    def turn(direction):
        return f'повернула({direction})'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Внимание! рекомендоманная скорость = 60, текущая = {self.speed}'
        return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Внимание! рекомендоманная скорость = 40, текущая = {self.speed}'
        return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


autos = [
    TownCar(65, 'Белый', 'Kia'),
    SportCar(130, 'Черный', 'Audi'),
    WorkCar(40, 'Красный', 'Lada'),
    PoliceCar(90, 'Белый', 'Ford')
]

for auto in autos:
    r = random.randint(0, 3)
    if 0 == r:
        print(f'Машина {auto.name} {auto.go()}')
    elif 1 == r:
        print(f'Машина {auto.name} {auto.stop()}')
    elif 2 == r:
        print(f'Машина {auto.name} {auto.turn("налево")}')
    else:
        print(f'Машина {auto.name} едет прямо')
    if auto.is_police:
        print(f'Машина {auto.name} полицейская')

    print(f'Скорость {auto.name} = {auto.show_speed()}')

