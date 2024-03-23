# coding: utf-8
"""
@python version : python3.10
@file name      : 调用js代码解密.py
@date           : 2024/3/22 16:40
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
# pip install pyexecjs

import execjs

# coding: utf-8
"""
@python version : python3.10
@file name      : 逆向请求.py
@date           : 2024/3/22 11:28
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       :  获取请求体加密参数
"""

import requests
import time
from hashlib import md5

session = requests.session()
session.get('https://fanyi.youdao.com/index.html#/')

word = "apple"
key = "fsdsogkndfokasodnaso"  # 固定值
mysticTime = str(int(time.time()) * 1000)
s = f'client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key={key}'
md5_obj = md5(s.encode())
sign = md5_obj.hexdigest()
data = {
    "i": word,
    "from": "auto",
    "to": "",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": sign,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": mysticTime,
    "keyfrom": "fanyi.web",
    "mid": "1",
    "screen": "1",
    "model": "1",
    "network": "wifi",
    "abtest": "0",
    "yduuid": "abcdefg"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://fanyi.youdao.com/",
    "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1088350298.5964031; OUTFOX_SEARCH_USER_ID=-104466465@61.173.76.226"
}
res = session.post('https://dict.youdao.com/webtranslate', data=data, headers=headers)
ret = res.text  # 得到的是一个base64 变种，需要把 - 替换成 +，_ 替换成 /

# print(ret)  # 获取返回的原始数据

with open('解密.js', 'r', encoding='utf-8') as f:
    js_str = f.read()
decrypt_data = execjs.compile(js_str).call('decrypt', ret)
print(decrypt_data)
