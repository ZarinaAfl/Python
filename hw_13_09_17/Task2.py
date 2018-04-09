# Конвертер из римских цифр в десятичную запись (в виде функции)

rome_nums = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
             'IV': 4, 'I': 1}


def into_arabic_system(number):
    result = 0
    position = 0
    while position < len(number):  # проходим по 2 символа
        n1 = number[position]
        if len(number) == position + 1:
            key = n1
        else:
            n2 = number[position + 1]
            key = n1 + n2
        if key in rome_nums:
            result += rome_nums[key]
            if len(key) == 2:
                position += 1
        else:
            result += rome_nums[n1]

        position += 1

    return result


n = str(input())
print(into_arabic_system(n))
