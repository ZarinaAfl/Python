#import  my_classes
from my_classes import Car1, TeslaCar

a = Car1("red", "Lada", "1979")
print(a)
print (dir(a)) #list of all methods
print(Car1)
#текущее состояние программы (текущие значения всех переменных)

print(globals()) #all vars of program from current scope

print(a.__dict__) #все поля данного объекта

a._number_of_wheels = 4

print(a.__dict__)
print (a.__secret_code)

b=TeslaCar("Red", "Tesla", 2016)

print(b)


print (hasattr(a, "brand")) #check attribute
print(getattr(a, "brand", "TAZ2109")) #get attribute

print(a+b)