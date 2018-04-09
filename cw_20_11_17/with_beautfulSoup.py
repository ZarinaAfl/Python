from bs4 import BeautifulSoup
import requests

with open("size.html", 'r') as  f:
    str = f.read()

tree = BeautifulSoup(str, "lxml")
result = tree.select(".item")


news = requests.get("https://news.yandex.ru/")

news_tree = BeautifulSoup(news.text, "lxml")
news_result = news_tree.select(".story__title")


for i in news_result:
    print(i.text)

print(result)
print(news_tree)