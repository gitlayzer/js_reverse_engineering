# coding: utf-8
"""
@python version : python3.10
@file name      : get_data.py
@date           : 2024/3/29 13:30
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

with open('p.public','r',encoding='utf-8') as f:
    public_key_str = f.read()

rsa_pk = RSA.importKey(public_key_str)
rsa = PKCS1_v1_5.new(rsa_pk)
# 公钥加密
result = rsa.encrypt('123'.encode("utf-8"))
print(result)