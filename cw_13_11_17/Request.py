

'''
request.get вход пожда
        .post
        
response.
        :cvar
        
#На вход подается список URL(картинки). Скачать их все
Pool

'''
import multiprocessing
import shutil

import requests

def download(url):
    file_req = requests.get(url)
    with open(url, "images") as receive:
        shutil.copyfileobj(file_req, requests)

url1 = "https://image.slidesharecdn.com/pyworks-1229584486232623-1/95/multiprocessing-with-python-36-728.jpg"
url2 = "https://i.ytimg.com/vi/_1ZwkCY9wxk/maxresdefault.jpg"

lst = [url1, url2]


pool = multiprocessing.Pool()
pool.map()