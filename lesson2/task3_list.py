month = None
while month is None or month < 1 or month > 12:
    month = int(input('Введите цифру месяца от 1 до 12: '))

months_periods = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

print(f'{month} месяц - это {months_periods[month - 1]}')
