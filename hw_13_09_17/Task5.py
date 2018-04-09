def __nod__(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    return n1 + n2

class RationalFraction:
    def __init__(self, numerator=0, denominator=0):
        self.numerator = numerator
        self.denominator = denominator



    def __reduce__(self):
        nod = __nod__(self.numerator, self.denominator)
        return RationalFraction(self.numerator//nod, self.denominator//nod)

    def __add__(self, rf2):
        num_res = self.numerator*rf2.denominator+rf2.numerator*self.denominator
        den_res = self.denominator*rf2.denominator
        nod = __nod__(num_res, den_res)
        return RationalFraction(num_res//nod, den_res//nod)

    def __sub__(self, rf2):
        num_res = self.numerator*rf2.denominator-rf2.numerator*self.denominator
        den_res = self.denominator*rf2.denominator
        nod = __nod__(num_res, den_res)
        return RationalFraction(num_res//nod, den_res//nod)

    def __mul__(self, rf2):
        num_res = self.numerator*rf2.numerator
        den_res = self.denominator*rf2.denominator
        nod = __nod__(num_res, den_res)
        return RationalFraction(num_res//nod, den_res//nod)

    def __div__(self, rf2):
        num_res = self.numerator*rf2.denominator
        den_res = self.denominator*rf2.numerator
        nod = __nod__(num_res, den_res)
        return RationalFraction(num_res//nod, den_res//nod)

    def __str__(self):
        print("%s/%s") % (self.numerator, self.denominator)

    def __value__(self):
        return self.numerator/self.denominator

    def __eq__(self, rf2):
        n1 = self.__reduce__()
        n2 = rf2.__reduce__()
        return (n1.numerator==n2.numerator and n1.denominator==n2.denominator)

    def number_part(self):
        if self.numerator>=self.denominator:
            return  self.numerator//self.denominator
        else:
            return 0

    



