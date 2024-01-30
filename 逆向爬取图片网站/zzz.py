# coding: utf-8
import time

import requests
import json
import execjs

url = "https://api.zzzmh.cn/bz/v3/getData"
data = {
    "size": 24,
    "current": 1,
    "sort": 0,
    "category": 0,
    "resolution": 0,
    "color": 0,
    "categoryId": 0,
    "ratio": 0
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
    "Referer": "https://bz.zzzmh.cn/",
    "Content-Typ": "application/json;charset=UTF-8"
}
res = requests.post(url=url, json=data, headers=headers)
content = res.json()['result']

# 读取js文件，传入加密数据，进行解密
with open('z.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
# 通过js代码解析加密数据
raw_plain_data = execjs.compile(js_code).call('_0x58b5da', content)
plain_data = json.loads(raw_plain_data)
images_data_list = plain_data['list']
# 拼接图片url
for image in images_data_list:
    t = image['t']
    i = image['i']
    image_url = f"https://api.zzzmh.cn/bz/v3/getUrl/{i}{t}9"
    image_content = requests.get(url=image_url, headers=headers).content
    with open(f'{i}.jpg', 'wb') as f:
        f.write(image_content)
        print(f"{i}.jpg 下载完成")
        time.sleep(0.5)
