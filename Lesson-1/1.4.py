# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode).

ENC_STR = 'разработка'
print(type(ENC_STR))
ENC_STR_BYTES = ENC_STR.encode('utf-8')
print(ENC_STR_BYTES)
print(type(ENC_STR_BYTES))
DEC_STR = ENC_STR_BYTES.decode('utf-8')
print(DEC_STR)

print('----------------------------------------------------')

ENC_STR = 'администрирование'
print(type(ENC_STR))
ENC_STR_BYTES = ENC_STR.encode('utf-8')
print(ENC_STR_BYTES)
print(type(ENC_STR_BYTES))
DEC_STR = ENC_STR_BYTES.decode('utf-8')
print(DEC_STR)

print('----------------------------------------------------')

ENC_STR = 'protocol'
print(type(ENC_STR))
ENC_STR_BYTES = ENC_STR.encode('utf-8')
print(ENC_STR_BYTES)
print(type(ENC_STR_BYTES))
DEC_STR = ENC_STR_BYTES.decode('utf-8')
print(DEC_STR)

print('----------------------------------------------------')

ENC_STR = 'standard'
print(type(ENC_STR))
ENC_STR_BYTES = str.encode(ENC_STR, encoding='utf-8')
print(ENC_STR_BYTES)
print(type(ENC_STR_BYTES))
DEC_STR = bytes.decode(ENC_STR_BYTES, encoding='utf-8')
print(DEC_STR)