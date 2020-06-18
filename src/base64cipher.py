import base64


# encode
def encodeMsg(msg):
    message_bytes = msg.encode('ascii', 'ignore')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii', 'ignore')
    return base64_message


def decodeMsg(Msg):
    #base64_bytes = Msg.encode('ascii', 'ignore')
    message_bytes = base64.b64decode(Msg)
    message = message_bytes.decode('ascii', 'ignore')
    return message

# print(decodeMsg('UyAJIDIzNzM2MjcxOCAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==SCAJIDIzNzM2MjgxMiAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==RSAJIDIzNzM2MjkwNiAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==TCAJIDIzNzM2MzA2MiAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==TCAJIDIzNzM2MzIwMyAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==WSAJIDIzNzM2MzMxMiAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==QmFjayAJIDIzNzM3MDgxMiAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==QmFjayAJIDIzNzM3MTM0MyAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==QmFjayAJIDIzNzM3MTY1NiAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==QmFjayAJIDIzNzM3MTgyOCAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==QmFjayAJIDIzNzM3MTk2OCAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg==QmFjayAJIDIzNzM3MjM0MyAJIGtleWxvZ2dlci1oYWNrLXB5dGhvbiAga2V5bG9nZ2VyLnB5IFB5Q2hhcm0gCg=='))
