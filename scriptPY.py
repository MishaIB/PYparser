import json
import os
import requests
from bs4 import BeautifulSoup
import time
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
def save_img(img_data,subdir,image_number):
     with open(f'dataset/{subdir}/{image_number}.jpg','wb') as file:
                file.write(img_data)
def create_file(subdir):
    if not os.path.exists(f'dataset/{subdir}'):
        os.makedirs(f'dataset/{subdir}')

def search_images():
    subdir='cat'
    page_number=0
    url=f'https://yandex.ru/images/search?p={page_number}&text=cat&uinfo=sw-1536-sh-864-ww-760-wh-754-pd-1.25-wp-16x9_1920x1080&lr=51&rpt=image'
    detour=0
    while True:
        create_file(subdir)
        image_number=1
        while image_number<50:
            time.sleep(2)
            response=requests.get(url,headers=headers).text
            soap= BeautifulSoup(response,"html.parser")
            links=soap.find_all("img",class_="serp-item__thumb justifier__thumb")
            for link in links:
                link = link.get("src")
                urls='https:'+ link
                img_data=requests.get(urls,verify=False).content
                save_img(img_data,subdir,image_number)
                image_number+=1
                print(f'изображение {image_number}.jpg успешно скачено')
            page_number+=1
        detour+=1    
        if detour>2:
            print('КОНЕЦ')
            break
        else:
            url=f'https://yandex.ru/images/search?p={page_number}&text=dog&lr=51&rpt=image'
            page_number=0
            subdir='dog'

def main():
    search_images()
    


