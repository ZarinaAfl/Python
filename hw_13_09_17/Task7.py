dictionary = {}
with open('text_for_task7.txt', 'r', encoding='UTF-8') as file_object:
    for line in file_object:
        for word in line.split():
            word = word.upper()
            if dictionary.__contains__(word):
                dictionary[word]+=1
            else:
                dictionary.__setitem__(word, 1)
    print(dictionary)