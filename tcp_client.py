import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("Server IP",8080))

data = "Hello"

s.send(data.encode())