# Дан файл с английским текстом. Выцепить список уникальных слов, без учета регистра.

dictionary = set()
with open('text.txt', 'r', encoding='UTF-8') as file_object:
    for line in file_object:
        line = line.rstrip('!:;,?)].\'}>\"\n')
        line = line.lstrip('{[\'(\"')
        for word in line.split():
            word = word.rstrip('!:;,?)].\'}>\"')
            word = word.lower()
            dictionary.add(word)
print(dictionary)



