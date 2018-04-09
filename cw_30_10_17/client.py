import socket

HOST = 'localhost'
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(b"HI, ITIS")
data = s.recv(4)
print(data)
s.close()