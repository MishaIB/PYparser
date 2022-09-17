import json
import os
import requests
from bs4 import BeautifulSoup
url='https://yandex.ru/images/search?text=cat&suggest_reqid=636214838166082117398516367577478'
subdir='cat'
while True:
    image_number=1
    response=requests.get(url,headers={"User-Agent":"Mozilla/5.0"}).text
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
        with open(f'{subdir}/{image_number}.jpg','wb') as file:
            file.write(img_data)
        image_number+=1
        print(f'изображение {image_number}.jpg успешно скачено')
    if os.path.exists('dog')==True:
        print('КОНЕЦ')
        break
    else:
        url='https://yandex.ru/images/search?text=dog'
        subdir='dog'
    
    #
