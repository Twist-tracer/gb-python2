summary = 0
while True:
    numbers = input('Введите числа через пробел: ').split()

    input_not_number = False
    for number in numbers:
        try:
            number = float(number)
        except ValueError:
            input_not_number = True
            break

        summary += float(number)

    print(f'Сумма: {summary}')

    if input_not_number:
        break
