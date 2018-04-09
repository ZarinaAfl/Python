import requests
import re



current_year = 1969
template = r'(\d{0,2}\s\w+)|(\w+\s\d{0,2},)\s[1-2]\d{3}'
count = 0


for i in range (1, 8031):
    doc = requests.get("https://www.rfc-editor.org/rfc/rfc" + i.__str__() + ".txt").text
    result = re.search(template, doc)

    if result is not None:
        date = result.group(0)
        length = len(date)
        year = date[length - 4: length]
        print(current_year.__str__())
        print(year)
        if (current_year.__str__() == year):
            count = count + 1
        else:
            if current_year.__str__() > year:
                print("Документ без года")
            else:
                print(current_year.__str__() + ': ' + '*' * count)
                current_year = current_year + 1
                count = 1
    else:
        print("Документ без года")






