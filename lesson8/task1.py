class Date:
    date_string = None

    def __init__(self, date_string):
        self.__class__.date_string = date_string

    @classmethod
    def to_tuple(cls):
        if not cls.validate(cls.date_string):
            return 'Invalid date!'

        day, month, year = cls.date_string.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def validate(date_string):
        try:
            day, month, year = date_string.split('-')

            day = int(day)
            month = int(month)
            year = int(year)
        except:
            return False

        if month < 1 or month > 12:
            return False

        leap_year = year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)  # високосный

        if month in (1, 3, 5, 7, 8, 10, 12):
            days_in_mouth = 31
        elif month in (4, 6, 9, 11):
            days_in_mouth = 30
        else:
            days_in_mouth = 29 if leap_year else 30

        return 0 < day <= days_in_mouth


print(Date('132-05-2020').to_tuple())
print(Date('13-41-2020').to_tuple())
print(Date('00-41-2020').to_tuple())
print(Date('18-00-2020').to_tuple())
print(Date('13-05-2021').to_tuple())
print(Date('30-02-2020').to_tuple())
print(Date('29-02-2020').to_tuple())
print(Date('29-02-2020s').to_tuple())
