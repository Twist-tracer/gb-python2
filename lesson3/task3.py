def my_func(arg1, arg2, arg3):
    numbers = [arg1, arg2, arg3]
    numbers.sort(reverse=True)
    return numbers[0] + numbers[1]


print(my_func(19, 4, 7))
print(my_func(-8, 12, -1))
print(my_func(0, 21, 3))
