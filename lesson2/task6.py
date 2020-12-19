products = []
while True:
    answer = input('Добавить товар? (д|н): ')

    if answer.lower() == 'н':
        break
    elif answer.lower() == 'д':
        product_number = int(input('Введите номер товара: '))

        product = {
            'название': input('Введите название товара: '),
            'цена': int(input('Введите цену товара: ')),
            'количество': int(input('Введите кол-во товара: ')),
            'eд': input('Введите единицу измерения: '),
        }

        products.append((product_number, product))
    else:
        continue

stats = {}
for product_number, product in products:
    for k in product:
        if k not in stats:
            stats[k] = set()

        stats[k].add(product[k])

for k in stats:
    stats[k] = list(stats[k])

print(stats)
