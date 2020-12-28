from functools import reduce

my_list = [number for number in range(100, 1001) if number % 2 == 0]

print(my_list)
print(reduce(lambda carry, item: carry + item, my_list))
