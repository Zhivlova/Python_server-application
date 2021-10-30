import sys
import os
import unittest
import json
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING
from common.utils import get_message, send_message

class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestMessage(unittest.TestCase):
    message = {
        'ACTION: PRESENCE',
        'TIME: 2.2',
        'USER: test'}
    message_ok = 'RESPONSE: 200'
    message_err = 'RESPONSE: 400'

    def test_get_message(self):
        test_sock_ok = TestSocket(self.message_ok)
        test_sock_err = TestSocket(self.message_err)
        self.assertEqual(get_message(test_sock_ok), self.message_ok)
        self.assertNotEqual(get_message(test_sock_err), self.message_err)

    if __name__ == '__main__':
        unittest.main()
        unittest.main()

    def test_send_message(self):

        test_socket = TestSocket(self.message)
        send_message(test_socket, self.message)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)
        self.assertRaises(TypeError, send_message, test_socket, "wrong_dictionary")

    if __name__ == '__main__':
        unittest.main()
        unittest.main()