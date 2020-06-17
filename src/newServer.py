import socket, threading, os
from time import sleep

host, port = "10.200.201.39", 4444


class transfer:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __init__(self, logFile):
        self.mysocket.bind((host, port))
        print(' Server is ready ..')
        self.mysocket.listen(5)
        self.conn, self.addr = self.mysocket.accept()

        self.logFile = logFile
        self.size = os.path.getsize(self.logFile)
        print(' file size : {}'.format(str(self.size)))
        threading.Timer(2, self.send_file).start()

    def send_file(self):
        with open(self.logFile, 'rb') as file:
            data = file.read(1024)
            self.conn.send(data)
            while data != bytes(''.encode()):
                # print(data)
                data = file.read(1024)
                self.conn.send(data)

            print(' File sent successfully.')


# Transfer = transfer()
