my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [v for k, v in enumerate(my_list) if k != 0 and v > my_list[k - 1]]

print(new_list)
