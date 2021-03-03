import socket

HOST = ''
POST = 13332

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, POST))
    s.sendall(b'Hello, World')
    data = s.recv(1024)
print('Received', repr(data))
