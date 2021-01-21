class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


positions = [
    Position(
        'Вася',
        'Пупкин',
        'Менеджер',
        {
            "wage": 60000,
            "bonus": 5000
        }
    ),
    Position(
        'Василий',
        'Суворов',
        'Программист',
        {
            "wage": 90000,
            "bonus": 8000
        }
    )
]

for position in positions:
    print(position.get_full_name(), position.get_total_income())
