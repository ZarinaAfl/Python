import multiprocessing


def f(lst):
    s = 0
    while (True):
        pass
    for i in range(1000):
            s += i*i
    print(s)


p = multiprocessing.Pool()
p.map(f, [1,2,3,4,5])
