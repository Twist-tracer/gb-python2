from random import randint
from functools import reduce

with open('task5.txt', 'w') as file:
    file.write(','.join([str(randint(0, 100)) for number in range(randint(1, 10))]))

with open('task5.txt', 'r') as file:
    numbers = [int(number) for number in file.read().split(',')]
    print(reduce(lambda carry, item: int(carry) + int(item), numbers))
