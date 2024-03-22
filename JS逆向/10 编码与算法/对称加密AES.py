# coding: utf-8
"""
@python version : python3.10
@file name      : 对称加密AES.py
@date           : 2024/3/21 15:45
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       :
"""

# ECB模式 不需要指定iv: 偏移量 ,CBC和 ECB一样，只需要加上一个iv参数，同key
from Crypto.Cipher import AES
from Crypto.Util.Padding import  pad,unpad #
import base64

key = "天若有情天!".encode()  # 加密key/解密key 为同一个key,必须为16位字节、24位字节、32位字节
# 1.加密并编码
plain_text = "df dfbdb .very good".encode()
aes = AES.new(key, AES.MODE_ECB)
# 如果text不足16位的倍数就用空格补足为16位
plain_text = pad(plain_text,16) #加密数据不够16位倍数自动填充
# while len(plain_text) % 16 != 0:
#     plain_text += b"\0"
# 加密

encrypt_data = aes.encrypt(plain_text)
# base64编码
base64_data_str = base64.b64encode(encrypt_data).decode()

# 2.解码并解密
# 解码
_encrypt_data = base64.b64decode(base64_data_str.encode())
# 解密
d_aes = AES.new(key, AES.MODE_ECB)
_plain_text = d_aes.decrypt(_encrypt_data)
print(unpad(_plain_text,16).decode()) # 去除填充的
