#!/usr/bin/env python
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    try:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(data.encode('utf-8'))
        received_data = tcpCliSock.recv(BUFSIZ)
        if not received_data:
            break
        print(received_data.decode('utf-8'))
    except KeyboardInterrupt:
        break

tcpCliSock.close()

