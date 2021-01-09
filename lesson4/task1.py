from sys import argv


def salary(hours, rate, award):
    return (hours * rate) + award


print(salary(int(argv[1]), int(argv[2]), int(argv[3])))
