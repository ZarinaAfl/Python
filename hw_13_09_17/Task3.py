#Вывести таблицу сложения для заданной цифры k (любой цикл). Т.е. на экране должно быть (например, для 3):

numeral = int (input())

for i in range (2, 10):
    print("{numeral}x{i} = {result}".format(
        numeral=numeral, i=i, result=numeral*i
    ))
