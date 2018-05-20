from jim import *


def test_f_encode():
    assert f_encode({"one": 'action'}) == b'{"one": "action"}'

def test_f_decode():
    a = f_encode({"one": 'action'})
    assert f_decode(a) == {'one': 'action'}