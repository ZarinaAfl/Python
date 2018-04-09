# Перебор с возвратом. Генетический алгоритм. Fitness function
# Есть строка идеал. Генерируем вариации. Сортируем по хорошести. Отбрасываем часть, скрещиваем между собой.
import random
import string

IDEAL = 'SHOP'
variants = set();


def generation():
    for i in range(100):
        leng = len(IDEAL)
        variants.add(random.choice(string.ascii_uppercase) for x in range(leng))


