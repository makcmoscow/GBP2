import client


def test_result():
    assert client.result({'response': 200, 'alert': 'OK'}) == 'OK'
    assert client.result({'response': 400, 'error': 'incorrect json object'}) == 'incorrect json object'