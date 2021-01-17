class OrganicCells:
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number

    def __add__(self, other):
        return OrganicCells(self.number + other.number)

    def __sub__(self, other):
        result = self.number - other.number

        if result > 0:
            return OrganicCells(result)
        else:
            print('Разница чисел меньше или равна 0')
            return self

    def __mul__(self, other):
        return OrganicCells(self.number * other.number)

    def __truediv__(self, other):
        return OrganicCells(int(self.number / other.number))

    def make_order(self, count_per_row):
        result = ''
        for i in range(1, self._number + 1):
            result += '*'

            if i % count_per_row == 0:
                result += '\n'

        return result


cells = OrganicCells(3)

cells += OrganicCells(4)
print(cells.number)

cells -= OrganicCells(2)
print(cells.number)

cells -= OrganicCells(15)
print(cells.number)

cells *= OrganicCells(7)
print(cells.number)

cells /= OrganicCells(3)
print(cells.number)

print(cells.make_order(5))
