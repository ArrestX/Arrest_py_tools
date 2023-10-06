import os
import requests
from bs4 import BeautifulSoup

url = 'https://wallhaven.cc/'
folder_name = 'new'

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for img in soup.find_all('img'):
    img_url = img.get('src')
    if img_url.endswith('.jpg'):
        response = requests.get(img_url)
        with open(os.path.join(folder_name, img_url.split('/')[-1]), 'wb') as f:
            f.write(response.content)
