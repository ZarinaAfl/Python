import random
# классы и функции могут быть пустыми
from abc import abstractmethod


class Car:
    pass

class Car1:
    def __init__(self, color, brand, year): #self is analogue this
        n = 0;
        self.color = color
        self.brand = brand
        self.year = year
        self.__secret_code=random.random()

    def start(self):
        print("Bibika is starting")

    def __str__(self):
        return "%s %s %s" % (self.color, self.brand, self.year)

    @classmethod
    def get_new_instance(cls):
        return Car(None, None, None)

    @abstractmethod
    def ride (self):
        pass

class TeslaCar(Car):
    def __init__(self, color, brand, year):
        super().__init__(color, brand, year)
        self.electricity = True

#Python's main
if __name__ == "__main__":
    print("My classes file")

