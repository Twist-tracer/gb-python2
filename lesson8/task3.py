class InvalidLiteral(ValueError):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


numbers = []

while True:
    user_input = input('Введите число или stop, для дого завершить программу: ')

    if user_input == 'stop':
        break

    try:
        if not is_number(user_input):
            raise InvalidLiteral('Введено не число!')

        numbers.append(user_input)
    except InvalidLiteral as e:
        print(e)

print(f'Введенные числа: {",".join(numbers)}')
