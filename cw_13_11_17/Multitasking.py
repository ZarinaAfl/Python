#GIL
'''
threading
multiprocessing
    mutex
    semaphore - контролирует, сколько потоков проходит через него. Взяв один,
    не позволяет пройти другим потокам

    lock.acquire - если один поток вызвал, то другой поток попытавшись
    взять require зависнет

    lock.release - отпуск блокировки. Сработает произвольный из тех, кто взял
    require

    Потоки. Класс t = Thread(target = f (функция, выполняемая в потоке,
                        args = () - значения, необходимые для запуска функции f)

'''

#Два потока, которые выводят на экран 10 рандомных чисел
import random

import  threading

import time


def random_number(name, e1, e2):
    for i in range(10):
        e1.wait() #ждет разрешения на работу
        print(name, random.randint(0, 5000))
        e1.clear() #засыпание первого
        e2.set() #пробуждение второго


e1 = threading.Event()
e2 = threading.Event()

t1 = threading.Thread(target = random_number("T1", e1, e2))
t2 = threading.Thread(target = random_number("T2", e2, e1))



d = time.time()
t1.start()
t2.start()

e1.set()

t1.join() #дожидаемся окончания потоков
t2.join()
print ("PAR", time.time() - d)


d = time.time()
random_number("T1")
print("SEC", time.time()-d)


