from functools import reduce

with open('task3.txt', 'r') as file:
    rows = [row.rstrip() for row in file.readlines()]
    persons = {}
    for row in rows:
        row_parts = [row_part.strip() for row_part in row.split(':')]
        persons[row_parts[0]] = int(row_parts[1])

print(f'Сотрудники {", ".join([person for person in persons if persons[person] < 20000])} зарабатывают меньше 20000')
print(f'Средняя зарплата: {reduce(lambda carry, item: carry + item, persons.values()) / len(persons)}')
