earnings = int(input('Введите выручку фирмы: '))
expenses = int(input('Введите расходы фирмы: '))

if earnings > expenses:
    print('Фирма получает прибыль :)')
    print(f'Рентабельность: {((earnings - expenses) / earnings) * 100}%')

    employees_count = int(input('Введите кол-во сотрудников: '))
    print(f'Каждый сотрудник приносит {(earnings - expenses) / employees_count} прибыли')
elif expenses > earnings:
    print('Фирма несет убытки :(')
else:
    print('Фирма работает в 0 :|')
