#Реализовать format(), которая принимает строку и именованные аргументы

def format(string, **kwargs):
    for k, v in kwargs.items():
        string = string.replace("{" + k + "}", v)
    return string



print(format("Student: {firstname} {lastname}", firstname='Bulat', lastname='Giniatullin'))