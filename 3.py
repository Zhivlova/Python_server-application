# 3. Задание на закрепление знаний по модулю yaml.
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует
# список, второму — целое число, третьему — вложенный словарь, где значение каждого
# ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);

DATA = {'action_list': ['msg_1', 'msg_2', 'msg_3'], 'number': 1,
        'to_list': {'name1': '€Ali', 'name2': '©Nick', 'name3': '©Bob'}}
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
# а также установить возможность работы с юникодом: allow_unicode = True;

import yaml

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(DATA, f_n, default_flow_style=False, allow_unicode=True)

# по умолчанию default_flow_style=False - Так считываемые данные выглядят более понятно

# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными

with open('file.yaml', encoding='utf-8') as f_n:
    F_N_CONTENT = yaml.load(f_n, Loader=yaml.FullLoader)
    print(F_N_CONTENT)
