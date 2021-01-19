from abc import ABCMeta, abstractmethod


class Dress(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def tissue(self):
        pass


class Coat(Dress):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    @property
    def tissue(self):
        return self._size / 6.5 + 0.5


class Suit(Dress):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    @property
    def tissue(self):
        return 2 * self._height + 0.3


coat = Coat('GUCCI', 48)
suit = Suit('Calvin Klein', 46)

print(coat.tissue)
print(suit.tissue)
