# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
# определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий
# новый «отчетный» файл в формате CSV.
# a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью
# регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС»,
# «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы»,
# «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде
# списка и поместить в файл main_data (также для каждого файла);
import csv
import re

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
os_list = [os_prod_list, os_name_list, os_code_list, os_type_list]
main_data = []
main_data.append(headers)


def get_data():
    for i in range(1, 4):
        with open('info_1.txt', encoding='utf-8') as file:
            data = file.read()

    os_prod_new = re.compile('Изготовитель системы')
    os_list.append(os_prod_new.re.findall(data))
    os_name_new = re.compile('Название ОС')
    os_list.append(os_name_new.re.findall(data))
    os_code_list = re.compile('Код продукта')
    os_list.append(os_code_list.re.findall(data))
    os_type_list = re.compile('Тип системы')
    os_list.append(os_type_list.re.findall(data))

    for x in range(len(os_list[0])):
        main_data.append([os_prod_list[x], os_name_list[x], os_code_list[x], os_type_list[x]])
    return main_data

get_data()

# b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(), а также
# сохранение подготовленных данных в соответствующий CSV-файл;

def write_to_csv(from_file):
    main_data = get_data()
    with open(from_file, 'w', encoding='utf-8') as f_n:
        F_N_READER = csv.reader(f_n)
        for row in F_N_READER:
            print(row)

# c. Проверить работу программы через вызов функции write_to_csv().
write_to_csv('1.csv')
