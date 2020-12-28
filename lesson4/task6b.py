from itertools import cycle
from datetime import datetime
import hashlib

now = datetime.now()
md5 = hashlib.md5()
md5.update(str(now.timestamp()).encode('utf-8'))
chars = md5.hexdigest()
chars = cycle(chars)
stop_chars = [1, 6, 7, 8, 9, 'a', 'e', 'f']
new_chars = ''
char = None
while char not in stop_chars:
    char = next(chars)
    new_chars += char

print(new_chars)
