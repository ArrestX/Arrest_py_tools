import requests
import json
import time
import os
import pandas as pd
import argparse

# 添加命令行参数处理
parser = argparse.ArgumentParser(description="Monitor GitHub repositories based on a query parameter.")
parser.add_argument("-i", "--input", help="Custom monitoring parameter.", required=True)
args = parser.parse_args()

query_param = args.input

time_sleep = 20  # 每隔20秒爬取一次

while (True):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25  Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
    }

    datas = []
    response = None

    if os.path.exists("olddata.csv"):
        df = pd.read_csv("olddata.csv", header=None)
        datas = df.where(df.notnull(), None).values.tolist()  # 将提取出来的数据中的nan转化为None
        response = requests.get(
            url=f"https://api.github.com/search/repositories?q={query_param}&sort=updated&per_page=10", headers=headers)
    else:
        response = requests.get(
            url=f"https://api.github.com/search/repositories?q={query_param}&sort=updated&order=desc", headers=headers)

    data = json.loads(response.text)

    for item in data["items"]:
        s = {"name": item['name'], "html": item['html_url'], "description": item['description']}
        s1 = [item['name'], item['html_url'], item['description']]
        if s1 not in datas:
            params = {
                "text": s["name"],
                "desp": " 链接:" + str(s["html"]) + "\n简介" + str(s["description"])
            }
            print("当前推送为" + str(s) + "\n")
            print(params)
            requests.get("https://sc.ftqq.com/SCT225637T4OfruMKkQB5WxdneaqZxJ5bF.send",
                         params=params, timeout=10)
            time.sleep(1)  # 以防推送太猛
            print("推送完成!")
            datas.append(s1)

    pd.DataFrame(datas).to_csv("olddata.csv", header=None, index=None)
    time.sleep(time_sleep)
