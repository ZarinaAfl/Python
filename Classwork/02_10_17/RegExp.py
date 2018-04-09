import re


# 00-23  00-59  00-59
def find(str):
    template = r"(([01]\d|2[0-3])\:([0-5]\d)\:([0-5]\d))"
    for m in re.finditer(template, str):

        h = m.group(1)
        if (h[0] == '0'):
            h = int(h[1] * 3600)
        else:
            h = int(h[1] * 3600)

        min = m.group(2)
        if (m[0] == '0'):
            min = int(m[1] * 60)
        else:
            min = int(min * 60)

        sec = m.group(3)
        if (sec[0] == '0'):
            sec = int(sec[1] * 60)
        else:
            sec = int(sec * 60)

        sum = sum + h + min + sec
        count = count + 1
        print(m.group(0))


def average_time():
    at = int(sum / count)
    h = int(at / 3600)
    m = at - h * 3600 / 60
    s = at - h * 3600 - m * 60
    print(h + ":" + m + ":" + s)


with open('text.txt', 'r', encoding='UTF-8') as file_object:
    sum = 0
    count = 0
    for line in file_object:
        find(line)

    average_time()
