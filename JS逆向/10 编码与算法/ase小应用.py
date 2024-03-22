# coding: utf-8
"""
@python version : python3.10
@file name      : ase小应用.py
@date           : 2024/3/21 16:47
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests
from Crypto.Cipher import AES
# 获取key

res = requests.get('https://v4.dious.cc/20220514/sxQc8O3m/1200kb/hls/key.key')
key = res.content

res2 = requests.get('https://v4.dious.cc/20220514/sxQc8O3m/1200kb/hls/zyLu92KC.ts')
with open('a.mp4','wb') as f:
    encrypt_data = res2.content
    aes = AES.new(key,AES.MODE_CBC,b'0000000000000000')
    plain_data = aes.decrypt(encrypt_data)
    f.write(plain_data)