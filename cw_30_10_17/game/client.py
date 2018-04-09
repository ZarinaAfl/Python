import socket

HOST = input("Enter host for connection ")
PORT = 1235
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

id = int(s.recv(1))
print("Your name is Player{}".format(id))
print(s.recv(12))

in_data = None
while in_data != b'game ends':
    damage = int(input('kick '))
    b = bytes("{} {}".format(id, damage), encoding='utf-8')
    s.sendall(b)
    in_data = s.recv(15)
    print(in_data)
results = s.recv(15)
print(results)
#192.168.43.126
#raise ValueError() обработка исключений try, except
'''
    try:
    except ValueErro:
    else: - если try успешен
    finally
    ДЗ: Написать любую мат. функцию на натуральных числах
    если не целое число, то выкинуть TypeError
    если целое, но не натуральное ValueError
    функция repr-вывод строк в исходном виде
'''