# coding: utf-8
import base64
from urllib.parse import urlencode
import requests
import time
import execjs
import json
from hashlib import md5
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

t = str(int(time.time()) * 1000)

with open('1.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

d = execjs.compile(js_code).call('getUuid')

data_dict = {"limit": "20", "page": "1"}  # 第几页，每页多少行
data_str = urlencode(data_dict)

with open('2.js', 'r', encoding='utf-8') as f2:
    js_code_3 = f2.read()
e = execjs.compile(js_code_3).call('get_e', data_str)
m = md5()
m.update(f"{e}{d}{t}".encode())
sign = m.hexdigest()
print(sign, t, d, data_str)

url = 'https://api.birdreport.cn/front/activity/search'
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Requestid': d,
    'Referer': 'http://pms.birdreport.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Sign': sign,
    'Timestamp': t,
}

# 获取请求体加密数据
with open('2.js', 'r', encoding='utf-8') as f:
    js_2_code = f.read()
encrypt_params = execjs.compile(js_2_code).call('get_encrypt_params', e)
print(encrypt_params)
print(headers)
res = requests.post(url, headers=headers, data=encrypt_params, timeout=10)
print(res.text)
