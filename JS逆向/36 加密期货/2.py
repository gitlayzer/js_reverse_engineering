# coding: utf-8
"""
@python version : python3.10
@file name      : 2.py
@date           : 2024/4/28 17:02
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests
import execjs

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cache-ts': '1714293742390',
    'encryption': 'true',
    'language': 'zh',
    'origin': 'https://www.coinglass.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.coinglass.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

params = {
    'symbol': 'BTC',
}

response = requests.get('https://capi.coinglass.com/api/openInterest/ex/info', params=params, headers=headers)
user = response.headers.get('user')
encrypt_data = response.json()['data']
url = "/api/openInterest/ex/info"
plain_data = execjs.compile(open("1.js", "r", encoding="utf-8").read()).call("get_r", url, user, encrypt_data)
print(plain_data)
