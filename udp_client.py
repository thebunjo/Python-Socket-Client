import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = "Message"

s.sendto(data.encode(), ("Server IP",8080))