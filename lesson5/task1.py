with open('task1.txt', 'w') as file:
    while True:
        string = input('Введите текст: ')

        if string == '':
            break

        file.write(string + '\n')
