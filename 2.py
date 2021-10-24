# 2. Задание на закрепление знаний по модулю json.
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
# количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f_n:
        data = json.load(f_n)
        print(type(data))
        print(data)
    DICT_TO_JSON = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json', 'w', encoding='utf-8') as f_o:
        orders= data['orders']
        print(type(orders))
        print(orders)
        orders.append(DICT_TO_JSON)
    with open('orders.json', 'w', encoding='utf-8') as f_o:
        json.dump(data, f_o, sort_keys=True, indent=4)

with open('orders.json', 'w', encoding='utf-8') as f_o:
    json.dump({'orders': []}, f_o, sort_keys=True, indent=4)

write_order_to_json('Macbook', '1', '216000', 'Mike', '04.03.2021')
write_order_to_json('Asus', '1', '110000', 'Sam', '14.08.2021')
write_order_to_json('Sony', '1', '190000', 'Kate', '21.11.2021')
