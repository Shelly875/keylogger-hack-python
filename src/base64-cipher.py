import base64

# encode
message = "Hello World! 124!"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

# decode
message = "SGVsbG8gV29ybGQhIDEyNCE="
base64_bytes = message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')
print(message)