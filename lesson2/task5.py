rating = [7, 5, 3, 3, 2]

number = None
while number is None or number < 1:
    number = int(input('Введите натуральное число'))

rating.append(number)
rating.sort(reverse=True)

print(rating)
