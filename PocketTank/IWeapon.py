from abc import ABCMeta, abstractmethod

#Interface
class Weapon(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def shoot(self): pass

    #разрыв снарядаpno
    @abstractmethod
    def animation(self): pass
