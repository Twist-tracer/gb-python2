with open('task2.txt', 'r') as file:
    rows = file.readlines()

    rows_count = len(rows)
    print(f'Количество строк в файле : {rows_count}')

    for row in rows:
        row = row.rstrip()
        print(f'Кол-во слов в строке "{row}" - {len(row.split())}')
