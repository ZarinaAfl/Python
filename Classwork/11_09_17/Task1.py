#Функция, которая суммирует произв. кол-во целых чисел

#encoding: utf-8

def f(*args):
    s = 0
    for item in args:
        s += item
    return s

print(f(20, 30, 20))
# [] - изменяемый список(list). () - неизменяемый список (кортеж/tuple). Позиционные, именованные аргументы(*произвольное количество).




# **kwargs ключ-значение (словарь)

def f2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

f2(student='Zarina', course='Informatika', teacher='Khasianov', mark='5')


def process(data):
    x=data[0]
process((1,)) #кортеж с одним числом
