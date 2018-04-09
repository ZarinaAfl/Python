import os

f = 1
command = str(input())
while f == 1:
    com = command.split()[0]
    if com == "exit":
        f = 0
    elif com == "ls"|"dir":
        print(os.listdir(os.curdir))
    elif com == "cd":
        os.chdir(os.curdir+command.split()[1])
    elif com == "cat":
        file = open(command.split()[1], 'w')
        print(f)
    else:
        print("Error")


