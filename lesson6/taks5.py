class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')


stationeries = [
    Pen('Шариковая ручка'),
    Pencil('Мягкий карандаш'),
    Handle('Спиртовой маркер'),
]

for stationery in stationeries:
    print(stationery.title)
    stationery.draw()
    print()
