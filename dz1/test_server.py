import server
from time import time


# def test_parser():
#     x = server.f_parser()
#     assert  x.port == '7777'

# print((server.f_parser().__dict__['port']))

def test_prepare():
    assert server.prepare({'action': 'presence'})['response'] == 200
    assert server.prepare({'action': 'presence'})['alert'] == 'OK'
    assert server.prepare({'action': 'nce'})['error'] == 'incorrect json object'
    assert server.prepare({'action': None})['error'] == 'incorrect json object'