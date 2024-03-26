# coding: utf-8
import base64
from urllib.parse import urlencode
import requests
import time
import execjs
import json
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
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

res = requests.post(url, headers=headers, data=encrypt_params, timeout=10)
encrypt_data = json.loads(res.content)['data']
print(encrypt_data)

# 获取key ,iv

# 通过调试不同页面，发现key 和iv 是固定值，接下来通过AES，cbc模式解密

key_str = '3583ec0257e2f4c8195eec7410ff1619'
iv_str = 'd93c0d5ec6352f20'
aes = AES.new(key_str.encode(), AES.MODE_CBC, iv_str.encode())

pad_data = pad(encrypt_data.encode(), 16)
decrypt_data = aes.decrypt(pad_data)
# print(decrypt_data.decode('utf-8', 'ignore'))
unpad_data = unpad(decrypt_data, 16)
print(unpad_data)
