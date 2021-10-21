# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

FILE = open('test_file.txt', 'w', encoding='utf-8')
FILE.write('сетевое программирование сокет декоратор')
FILE.close()
print(type(FILE))
print(FILE)

default_encoding = locale.getpreferredencoding()
print(default_encoding)

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')

#cp1251
# сетевое программирование сокет декоратор