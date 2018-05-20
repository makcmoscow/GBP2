import socket
import argparse

from type_msg import *
import jim


def f_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default='7777')
    parser.add_argument('-a', '--address', default='127.0.0.1')
    return parser.parse_args()

def recv(sock):
    bjmessage = sock.recv(1024)
    return bjmessage

def prepare(data):
    try:
        if data['action'] == 'presence':
            return f_alert(200, code['200'])
        else:
            return f_error(400, code['400'])
    except KeyError:
        return f_error(400, code['400'])

def send(sock, bjmessage):
    sock.send(bjmessage)

###
if __name__ == '__main__':
    args = f_parser()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((args.address, int(args.port)))
        serv_sock.listen(10)
        # sock.settimeout(200) #потому что без цикла по таймауту сервер-сокет умирает
        while True:
            conn, addr = serv_sock.accept()
            print('Поступил запрос на подключение от: {}'.format(addr))
            message = recv(conn)
            response = prepare(jim.f_decode(message))
            send(conn, jim.f_encode(response))



