from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        colors = cycle(['красный', 'желтый', 'зеленый'])
        self.__color = next(colors)

        while True:
            print(self.__color)

            if self.__color == 'красный':
                sleep(7)
            elif self.__color == 'желтый':
                sleep(2)
            elif self.__color == 'зеленый':
                sleep(3)

            self.__color = next(colors)


traffic_light = TrafficLight()
traffic_light.running()
