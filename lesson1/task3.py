num = None

while not ((num is not None) and (0 <= num <= 9)):
    try:
        num = int(input('Введите число от 0 до 9 включительно: '))
    except ValueError:
        pass

result = []
for i in range(num):
    result.append(int(str(num)*(i+1)))

print(f'{" + ".join(map(lambda num: str(num), result)) if num > 0 else 0} = {sum(result)}')
