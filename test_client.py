import sys
import json
import socket
import time
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message

import unittest


class TestCreateRequestPresence(unittest.TestCase):
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_presence(self):
        out = {
            ACTION: PRESENCE,
            DEFAULT_PORT: 7777,
            TIME: 2.2,
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }
        return out
        self.assertEqual(out, ['PRESENCE', 7777, 2.2, 'Guest'])


if __name__ == '__main__':
    unittest.main()

print('----------------------------------------------------')


class TestPresenceAns(unittest.TestCase):
    def test_presence_ok(self):
        self.assertEqual(presence_ans({RESPONSE: 200}), '200 : OK')

    def test_presence_error(self):
        self.assertEqual(presence_ans({RESPONSE: 400, ERROR: 'ERROR_no_RESPONSE'}), '400 : ERROR_no_RESPONSE')


if __name__ == '__main__':
    unittest.main()
    unittest.main()

print('----------------------------------------------------')






"""Программа-клиент"""

def create_request_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    """
    out = {
        ACTION: PRESENCE,
        DEFAULT_PORT: 9000,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def presence_ans(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    """Загружаем параметы коммандной строки"""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_request_presence()
    send_message(transport, message_to_server)
    try:
        answer = presence_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
