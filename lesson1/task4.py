num = None

while not ((num is not None) and (0 < num)):
    try:
        num = int(input('Введите целое положительное число: '))
    except ValueError:
        pass


result = 0
while num > 0:
    if (num % 10) > result:
        result = num % 10

    num //= 10

print(result)
