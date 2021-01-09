from itertools import count

number = 13
numbers = count(number)

while (number / 91 * 21) % 2 != 0:
    number = next(numbers)

print(number)
