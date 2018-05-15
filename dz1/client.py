import socket
import sys

from type_msg import *
import jim


def send(soc, bjmessage):
    soc.send(bjmessage)

def recv(soc):
    bjdata = soc.recv(1024)
    return bjdata

def resalt(data):
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

name = input('Введите ваше имя: ')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(param())
    data = jim.f_encode(f_presence(name))
    send(sock, data)
    response = recv(sock)

    print(resalt(jim.f_decode(response)))