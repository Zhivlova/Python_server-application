# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать
# в байтовом типе.

text = b'attribute'
text = 'attribute'.encode('unicode_escape')
print(type(text))
print(text)

print('----------------------------------------------------')

#text = b'класс'
# SyntaxError: bytes can only contain ASCII literal characters.
text = 'класс'.encode('unicode_escape')
print(type(text))
print(text)

print('----------------------------------------------------')

#text = b'функция'
# SyntaxError: bytes can only contain ASCII literal characters.
text = 'функция'.encode('unicode_escape')
print(type(text))
print(text)

print('----------------------------------------------------')

text = b'type'
text = 'type'.encode('unicode_escape')
print(type(text))
print(text)