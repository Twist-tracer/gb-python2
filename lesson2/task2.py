items = input('Укажите элементы списка через запятую: ').split(',')

items_copy = items.copy()
for k, v in enumerate(items):
    if len(items) % 2 == 0 or k != (len(items) - 1):
        if k % 2 == 0:
            items_copy[k + 1] = v
        else:
            items_copy[k - 1] = v
    else:
        items_copy[k] = v

items = items_copy.copy()
del items_copy

print(items)
