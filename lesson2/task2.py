items = input('Укажите элементы списка через запятую: ').split(',')

for k, v in enumerate(items):
    if len(items) % 2 == 0 or k != (len(items) - 1):
        if k % 2 == 0:
            items.append(v)
        else:
            items[k - 1] = v
            items[k] = items.pop()
    else:
        items[k] = v

print(items)
