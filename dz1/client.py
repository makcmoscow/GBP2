import socket
import sys

from type_msg import *
import jim


def send(sock, bjmessage):
    sock.send(bjmessage)

def recv(sock):
    bjdata = sock.recv(1024)
    return bjdata

def result(data):
    if data['response'] == 200:
        return data['alert']
    else:
        return data['error']

def param():
    addr = sys.argv[1]
    if sys.argv[2] == None:
        port = 7777
    else:
        port = int(sys.argv[2])
    return (addr, port)

if __name__ == '__main__':

    name = input('Введите ваше имя: ')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(param())
        pres = f_presence(name)
        data = jim.f_encode(pres)
        send(sock, data)
        response = recv(sock)

        print(result(jim.f_decode(response)))