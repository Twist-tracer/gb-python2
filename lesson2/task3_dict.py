month = None
while month is None or month < 1 or month > 12:
    month = int(input('Введите цифру месяца от 1 до 12: '))

months_periods = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}

print(f'{month} месяц - это {months_periods[month]}')
