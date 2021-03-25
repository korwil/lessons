# 2-e задание
from abc import ABC, abstractmethod


class Clothes(ABC):
    name = None

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    name = 'Пальто'

    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    name = 'Костюм'

    def __init__(self, growth):
        self.growth = growth

    @property
    def fabric_consumption(self):
        return 2 * self.growth + 0.3


c = Coat(65)
s = Suit(180)

print(f'Расход {c.name} с размером {c.size} = {c.fabric_consumption}')
print(f'Расход {s.name} с ростом {s.growth} = {s.fabric_consumption}')

