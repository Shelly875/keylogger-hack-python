import base64


# encode
def encodeMsg(msg):
    message_bytes = msg.encode('ascii', 'ignore')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii', 'ignore')
    return base64_message + '\n'


def decodeMsg(Msg):

    # base64_bytes = Msg.encode('ascii', 'ignore')
    message_bytes = base64.b64decode(Msg)
    message = message_bytes.decode('ascii', 'ignore')
    return message

# a = 'shelly\n'
# b = 'beni\n'
# c = 'liat\n'
# d = a+b+c
# print(d)
# e = encodeMsg(d)
# print(e)
# e = encodeMsg(a)
# f = encodeMsg(b)
# g = e+f
# print(g)
# print(decodeMsg(g))
