words = input('Введите текст: ').split(' ')

for num, word in enumerate(words):
    print(f'{num + 1}) {word[0:10]}')
