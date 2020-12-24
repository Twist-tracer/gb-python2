def my_func(x, y):
    return x**y


def my_func2(x, y):
    if y == 0:
        return 1

    if y == 1:
        return x

    result = x
    for i in range(abs(y) - 1):
        result *= x

    return 1 / result if y < 0 else result


x = float(input('Введите действительное положительное число: '))
if x <= 0:
    print('Число должно быть положительным')
    exit(0)

y = int(input('Введите целое отрицательное число: '))
if y >= 0:
    print('Число должно быть отрицательным')
    exit(0)

print(my_func(x, y), my_func2(x, y))
