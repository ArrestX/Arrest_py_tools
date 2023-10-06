import requests
from bs4 import BeautifulSoup
import os

url = "https://wallhaven.cc/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 创建 new 文件夹，如果已存在则不创建
if not os.path.exists("new"):
    os.makedirs("new")

# 遍历每个 span 标签
for span in soup.find_all("span"):
    # 在每个 span 标签中寻找 a 标签
    a_tag = span.find("a")
    if a_tag:
        # 在 a 标签中寻找 img 标签
        img_tag = a_tag.find("img")
        if img_tag:
            # 保存 img 标签的 src 属性值
            src = img_tag["src"]
            # 获取文件名
            filename = src.split("/")[-1]
            # 将文件保存到 new 文件夹
            with open(f"new/{filename}", "wb") as f:
                image = requests.get(src).content
                f.write(image)
