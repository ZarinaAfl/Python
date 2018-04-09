#селекторы - теги, айди, название класса, вызов атрибута
#язык xpath, библиотека lxml

'''
1. Способ
from lxml import html
tree = html.fromstring(txt) - превращает строку в древовидную архитектуру,
далее можно делать запросы к ней, использую xpath
result = tree.xpath("//div")

2. Способ
BeutifulSoup

from bs4 import BeautifulSoup
tree = BeautifulSoup(txt)
result = tree.find("div", {"class": "movielist"})
    .get("class")
    .select (".item")


def render(elem):
    if есть_дети:
        for child in elem:
            render(child)
    else:
        render_final(elem)
'''

from lxml import html, etree

with open("size.html", 'r') as  f:
    str = f.read()

tree = html.fromstring(str)
result = tree.xpath("//div")
for elem in result:
    print(etree.tostring(elem, pretty_print=True))