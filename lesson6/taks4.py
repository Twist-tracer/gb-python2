class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        print(f'Машина поревнула на {direction}')

    def show_speed(self):
        print('Скорость машины:', car.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()

        if self.speed > 60:
            print(f'Превышение на {self.speed - 60} км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()

        if self.speed > 40:
            print(f'Превышение на {self.speed - 40} км/ч!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


cars = [
    TownCar(
        58,
        'Синий',
        'Volkswagen polo'
    ),
    TownCar(
        73,
        'Зеленый',
        'Hyundai solaris'
    ),
    SportCar(
        242,
        'Ультрамарин',
        'Ferrari Portofino'
    ),
    WorkCar(
        18,
        'Желтый',
        'Трактор'
    ),
    WorkCar(
        53,
        'Желтый',
        'Комбайн'
    ),
    PoliceCar(
        87,
        'Синий',
        'Ford Focus'
    ),
]

for car in cars:
    print('Тип машины:', car.__class__.__name__)
    car.show_speed()
    print('Цвет машины:', car.color)
    print('Название машины:', car.name)
    print('Машина является полицейской?:', 'да' if car.is_police else 'нет')
    car.turn('лево')
    car.turn('право')
    print()
