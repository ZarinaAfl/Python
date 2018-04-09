dictionary = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0,
              'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

with open('text_for_task6.txt', 'r', encoding='UTF-8') as file_object:
    for line in file_object:
        line = line.rstrip('!:;,?)].\'}>\"\n')
        line = line.lstrip('{[\'(\"')
        for word in line.split():
            word = word.rstrip('!:;,?)].\'}>\"')
            word = word.upper()
            for letter in word:
                dictionary[letter]+=1
    print(dictionary)