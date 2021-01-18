# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time

RED = 'Красный'
YELOU = 'Желтый'
GREEN = 'Зеленый'


class TrafficLight:
    __color = RED
    __befor = GREEN

    def running(self, worktime):
        t = time.time()
        while time.time() < t + worktime:
            print(f'Цвет: {self.__color}')
            if self.__color == RED and self.__befor == GREEN:
                time.sleep(7)
                self.__set_color(self.__color, YELOU)
            elif self.__color == YELOU and self.__befor == RED:
                time.sleep(2)
                self.__set_color(self.__color, GREEN)
            elif self.__color == GREEN and self.__befor == YELOU:
                time.sleep(5)
                self.__set_color(self.__color, RED)
            else:
                print('Нарушение порядка')
                break

    def __set_color(self, befor, color):
        self.__befor = befor
        self.__color = color


# Альтернатива, правда без проверки порядка
class TrafficLight2:
    __color = {RED: 7, YELOU: 2, GREEN: 5}

    def running(self, worktime):
        t = time.time()
        while time.time() <= t + worktime:
            for col, ti in self.__color.items():
                print(f'Цвет: {col}')
                time.sleep(ti)


t = TrafficLight()
t.running(29)

t = TrafficLight2()
t.running(29)
