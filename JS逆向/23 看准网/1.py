# coding: utf-8
"""
@python version : python3.10
@file name      : 1.py
@date           : 2024/4/2 9:47
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

import json
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = 'G$$QawckGfaLB97r'
iv = 'OYQEOyYzzCCx5wYJ'  # 随机字符串，没有要求，从控制台随便拿一个s的值
# 最终可以将cityCode 最为参数传入
data = {"cityCode": 101280100, "industryCode": "", "curPage": 1, "establishYears": "", "registerCapitals": ""}
text = json.dumps(data).encode()
aes = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
# aes加密
b_data = aes.encrypt(pad(text, 16))
# base64转码,并作字符串替换
b_data_b64 = base64.b64encode(b_data).decode().replace('/', '_').replace('+', '-').replace('=', '~')

import requests

cookies = {
    'W_CITY_S_V': '1',
    'wd_guid': 'c335a9af-a23b-43eb-8f0e-9744b4a07edf',
    'historyState': 'state',
    'R_SCH_CY_V': '18048827|1978457',
    '__c': '1712020243',
    '__g': '-',
    '__l': 'l=%2Fwww.kanzhun.com%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DruWm4CDSrGiVijXvritMGuj35GDSZeAkIMnqqhVFdOmIWcTTx3LjOr0j2f1zKI3l%26wd%3D%26eqid%3Dabeb3212000083cc00000004660b5b12',
    'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1711950370,1712020249',
    '__lh_v1': '5_0',
    '__a': '24135332.1704163054.1711950370.1712020243.40.4.7.40',
    'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1712020408',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': 'W_CITY_S_V=1; wd_guid=c335a9af-a23b-43eb-8f0e-9744b4a07edf; historyState=state; R_SCH_CY_V=18048827|1978457; __c=1712020243; __g=-; __l=l=%2Fwww.kanzhun.com%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DruWm4CDSrGiVijXvritMGuj35GDSZeAkIMnqqhVFdOmIWcTTx3LjOr0j2f1zKI3l%26wd%3D%26eqid%3Dabeb3212000083cc00000004660b5b12; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1711950370,1712020249; __lh_v1=5_0; __a=24135332.1704163054.1711950370.1712020243.40.4.7.40; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1712020408',
    'href': 'https://www.kanzhun.com/rank_f/c101280600/',
    'pragma': 'no-cache',
    'referer': 'https://www.kanzhun.com/rank_f/c101280600/',
    'reqsource': 'fe',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceid': '08d12a13-cb97-4d75-8501-e121fcbe4794',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'b': b_data_b64,
    'kiv': iv,
}

response = requests.get(
    'https://www.kanzhun.com/api_to/channel/company/list.json',
    params=params,
    cookies=cookies,
    headers=headers,
)
# print(response.text)

encrypt_data = response.text

# 先进行base64解码
de_aes = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
de_b64_data = base64.b64decode(encrypt_data.encode())
# 解密
decrypt_data = de_aes.decrypt(de_b64_data)
# unpad
plain_data = unpad(decrypt_data,16).decode()
print(plain_data)