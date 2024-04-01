# coding: utf-8
"""
@python version : python3.10
@file name      : main.py
@date           : 2024/4/1 16:01
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import json
import base64

kiv = 'IKTDsaJ5so8ZLbHb'
aes_key = 'G$$QawckGfaLB97r'  # 从浏览器执行js代码获取的固定值  n.key.toString(o.enc.Utf8)

data = {"cityCode": 101280600, "industryCode": "", "curPage": 1, "establishYears": "", "registerCapitals": ""}
data_str = json.dumps(data).encode()

aes = AES.new(aes_key.encode('utf-8'), AES.MODE_CBC, kiv.encode('utf-8'))
aes_data = pad(data_str,16)
encrypt_b_data = aes.encrypt(aes_data)
# 对加密数据进行base64编码,并按照js源文件中变种修改
res = base64.b64encode(encrypt_b_data).decode('utf-8').replace("/", "_").replace("+", "-").replace("=", "~")


request_params = {
    'b' : res,
    "kiv" :kiv
}



cookies = {
    'W_CITY_S_V': '1',
    'wd_guid': 'c335a9af-a23b-43eb-8f0e-9744b4a07edf',
    'historyState': 'state',
    'R_SCH_CY_V': '18048827|1978457',
    '__c': '1711950370',
    '__g': '-',
    '__l': 'l=%2Fwww.kanzhun.com%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVT_2Cfzxp5XHBGADMSLfHqNL0EBT0ZD4IpwCsKitI92P7HdU4XgXUez2RGHv-qh9%26wd%3D%26eqid%3Dd9f20d220005b4f500000004660a4a1f',
    'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1711950370',
    '__lh_v1': '5_0',
    '__a': '24135332.1704163054.1704270367.1711950370.24.3.21.24',
    'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1711955347',
    'wbrwsid': '42307638',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': 'W_CITY_S_V=1; wd_guid=c335a9af-a23b-43eb-8f0e-9744b4a07edf; historyState=state; R_SCH_CY_V=18048827|1978457; __c=1711950370; __g=-; __l=l=%2Fwww.kanzhun.com%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVT_2Cfzxp5XHBGADMSLfHqNL0EBT0ZD4IpwCsKitI92P7HdU4XgXUez2RGHv-qh9%26wd%3D%26eqid%3Dd9f20d220005b4f500000004660a4a1f; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1711950370; __lh_v1=5_0; __a=24135332.1704163054.1704270367.1711950370.24.3.21.24; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1711955347; wbrwsid=42307638',
    'href': 'https://www.kanzhun.com/rank_f/c101020100/',
    'pragma': 'no-cache',
    'referer': 'https://www.kanzhun.com/rank_f/c101020100/',
    'reqsource': 'fe',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceid': '21f3910c-c587-4ecd-8709-c9425c65edf1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get(
    'https://www.kanzhun.com/api_to/channel/company/list.json',
    params=request_params,
    cookies=cookies,
    headers=headers,
)


# 可以浏览器全局搜索 interceptor 拦截器，定位 interceptor.response 获取解密方法的定位
# 解码解密
de_aes = AES.new(aes_key.encode('utf-8'), AES.MODE_CBC, kiv.encode('utf-8'))
base_64_decode = base64.b64decode(response.text.encode())
# aes 解密
res_data = de_aes.decrypt(base_64_decode)
print(unpad(res_data,16).decode())