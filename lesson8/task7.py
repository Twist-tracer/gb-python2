class ComplexNumber:
    def __init__(self, real, imagine):
        self.__real = real
        self.__imagine = imagine

    def __str__(self):
        return f'{self.__real}+i{self.__imagine}'

    def __add__(self, other):
        return ComplexNumber(self.__real + other.__real, self.__imagine + other.__imagine)

    def __mul__(self, other):
        return ComplexNumber(
            (self.__real * other.__real) - (self.__imagine * other.__imagine),
            (self.__real * other.__imagine) + (other.__real * self.__imagine)
        )


number = ComplexNumber(7, 6)
number_2 = ComplexNumber(4, 12)

print(f'{number} + {number_2} = {number + number_2}')
print(f'{number} * {number_2} = {number * number_2}')
