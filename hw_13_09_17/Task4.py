from cmath import sqrt

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __add__(self, v2):
        return Vector2D(self.x+v2.x, self.y+v2.y)

    def __sub__(self, v2):
        return Vector2D(self.x-v2.x, self.y-v2.y)

    def __mul_n__(self, number):
        return Vector2D(self.x*number, self.y*number)

    def __str__(self):
        return "({x}; {y})".format(
            x=self.x, y=self.y
        )

    def __len__(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def __mul__(self, v2):
        return self.x*v2.x + self.y*v2.y

    def __eq__(self, v2):
        k = self.x/v2.x
        return ((k == self.y/v2.y) and (k > 0) and (self.__len__() == v2.__len__()))




