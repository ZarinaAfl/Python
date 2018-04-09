import random

for p in range(0, 50):
    n = random.randint(1,5)
    name = ""
    for i in range (0,n):
        name += chr(random.randint(ord('A'), ord('Z')))
    f = open("%s.txt" %name, "w")
    f.write(str(random.random()))
    f.close()



