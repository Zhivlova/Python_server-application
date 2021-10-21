# 2. Каждое из слов «class», «function», «method» записать в байтовом типе
# без преобразования в последовательность кодов (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

STR = 'class'
print(type(STR))
ENC_STR_BYTES = bytes(STR, encoding='utf-8')
print(type(ENC_STR_BYTES))
print(ENC_STR_BYTES)
print(len(ENC_STR_BYTES))

print('----------------------------------------------------')

STR = 'function'
print(type(STR))
ENC_STR_BYTES = bytes(STR, encoding='utf-8')
print(type(ENC_STR_BYTES))
print(ENC_STR_BYTES)
print(len(ENC_STR_BYTES))

print('----------------------------------------------------')

STR = 'method'
print(type(STR))
ENC_STR_BYTES = bytes(STR, encoding='utf-8')
print(type(ENC_STR_BYTES))
print(ENC_STR_BYTES)
print(len(ENC_STR_BYTES))
