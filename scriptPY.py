import json
import os
import requests
from bs4 import BeautifulSoup
url='https://yandex.ru/images/search?text=cat&from=tabbar'
subdir='cat'
image_number=1
response=requests.get(url).text
soap= BeautifulSoup(response,"html.parser")
links=soap.find_all("img",class_="serp-item__thumb justifier__thumb")
if not os.path.exists('dataset'):
    os.mkdir('dataset')
if not os.path.exists(subdir):
    os.mkdir(subdir)
for link in links:
    link = link.get("src")
    urls='https:'+ link
    img_data=requests.get(urls,verify=False).content
    with open(f'cat/{image_number}.jpg','wb') as file:
        file.write(img_data)
    image_number+=1
    print(f'изображение {image_number}.jpg успешно скачено')
