input_seconds = int(input('Введите секунды: '))

second = 1
minute = (second * 60)
hour = (minute * 60)

hours = input_seconds // hour
minutes = (input_seconds % hour) // minute
seconds = (input_seconds % minute) // second

print(f'{input_seconds} секунд - это {hours}:{minutes}:{seconds}')
