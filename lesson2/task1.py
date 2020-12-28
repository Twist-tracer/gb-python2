items = [
    None,
    True,
    1,
    1.2,
    'string',
    b'bytes',
    ['item1', 'item2'],
    ('item1', 'item2'),
    {'item1', 'item2'},
    {'first': 'item1', 'second': 'item2'}
]

for item in items:
    print(type(item))
