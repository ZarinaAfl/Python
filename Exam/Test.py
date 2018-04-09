import requests
import re
template = r'\w+\s\d{0,2},\s\d{4}'

doc = requests.get("https://www.rfc-editor.org/rfc/rfc22.txt").text
result = re.search(template, doc)

print(result.group(0))