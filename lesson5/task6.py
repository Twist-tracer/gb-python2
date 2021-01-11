from functools import reduce

subjects = {}
with open('task6.txt', 'r') as file:
    for row in file.readlines():
        (subject, lessons) = row.split(':')

        lessons = [int(''.join([char for char in lesson if char.isdigit()])) for lesson in lessons.split(',')]
        subjects[subject] = reduce(lambda carry, item: carry + item, lessons)

print(subjects)
