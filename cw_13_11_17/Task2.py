import multiprocessing
import random

import  threading
import _multiprocessing
import time

#передача данных из одного потока в другой
def random_number(n, q):
    for i in range(n):
        r = random.randrange(100)
        q.put(r)
        print(r)



q = multiprocessing.Queue()
t1 = multiprocessing.Process(target = random_number, args = (10, q))

d = time.time()
t1.start()
print(time.time() - d)

while (q.empty() is False):
    print( "get:", q.get())


