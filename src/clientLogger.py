import socket

s = socket.socket()
s.connect(("10.200.201.39", 6666))

while True:
    print(s.recv(126).decode())
