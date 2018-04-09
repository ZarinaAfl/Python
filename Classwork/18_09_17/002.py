import os

s=0.0
for f in os.listdir("."):
    if f.__contains__(".txt"):
        if (f[0] in "aetion"):
            fn = open(f)
            number = float(fn.read())
            s+=number

print(s)