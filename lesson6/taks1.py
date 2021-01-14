from time import sleep
from itertools import cycle
from threading import Thread


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        colors = cycle(['красный', 'желтый', 'зеленый'])
        self.__color = next(colors)

        while True:
            if self.__color == 'красный':
                sleep(7)
            elif self.__color == 'желтый':
                sleep(2)
            elif self.__color == 'зеленый':
                sleep(3)

            self.__color = next(colors)

    def get_color(self):
        return self.__color


traffic_light = TrafficLight()
thread = Thread(target=traffic_light.running)
colors = cycle(['красный', 'желтый', 'зеленый'])
prev_color = current_color = assert_color = None
thread.start()
while current_color == assert_color:
    print(current_color)

    prev_color = current_color
    current_color = traffic_light.get_color()

    if prev_color != current_color:
        assert_color = next(colors)

    sleep(1)
else:
    print(f'Светофор сломан! Загорелся {current_color} вместо {assert_color}')
