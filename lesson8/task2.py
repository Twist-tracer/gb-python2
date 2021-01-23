number_1 = int(input('Введите делимое: '))
number_2 = int(input('Введите делитель: '))


class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self):
        self.__message = 'Деление на ноль недопустимо'

    def __str__(self):
        return self.__message


try:
    try:
        result = number_1 / number_2
    except ZeroDivisionError:
        raise MyZeroDivisionError

    print(f'{number_1} / {number_2} = {result}')
except MyZeroDivisionError as e:
    print(e)
