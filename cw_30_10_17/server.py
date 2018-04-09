import socket

HOST = ''
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

data = conn.recv(4)
print(data)
conn.sendall(b"abcd")