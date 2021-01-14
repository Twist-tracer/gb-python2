class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self, w_per_cm, cm):
        return self._length * self._width * w_per_cm * cm


road = Road(5000, 20)

print(f'{int(road.calc_weight(25, 5) / 1000)} т')
