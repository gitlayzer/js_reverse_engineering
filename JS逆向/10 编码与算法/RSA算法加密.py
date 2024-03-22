# coding: utf-8
"""
@python version : python3.10
@file name      : RSA算法加密.py
@date           : 2024/3/22 9:06
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
# rsakey = RSA.generate(1024)
# # 生成公私钥匙
# with open('ras.public','wb') as f:
#     f.write(rsakey.public_key().exportKey())
#
# # 生成私钥
# with open('ras.private','wb') as f:
#     f.write(rsakey.exportKey())


# 加密
data = "我喜欢你"
with open(r"C:\Users\杨子洋\PycharmProjects\spiders\JS逆向\10 编码与算法\ras.public", mode="r") as f:
    pk = f.read()
    rsa_pk = RSA.importKey(pk)
    rsa = PKCS1_v1_5.new(rsa_pk)

    result = rsa.encrypt(data.encode("utf-8"))
    # 处理成b64方便传输
    b64_result = base64.b64encode(result).decode("utf-8")
    print(b64_result)


# 解密
data = "jt8sLAPW03rFiPO/AZmQy3qPa/oQHWcFdQZcGBxqkBipiwGrsOzvrqVFQxqgqKN8rQf70ki4giHSxk7/N7B50h2y893itQOZOYxZICUxDQfaMXE8TW3wU5SWi9zcTSwHA4x+TsWvZSdxq4R1JsJjkUl6WYl5zaUbRaL9T7nt1JM="
# 解密
with open(r"C:\Users\杨子洋\PycharmProjects\spiders\JS逆向\10 编码与算法\ras.private", mode="r") as f:
    prikey = f.read()
    rsa_pk = RSA.importKey(prikey)
    rsa = PKCS1_v1_5.new(rsa_pk)
    result = rsa.decrypt(base64.b64decode(data), None)
    print("rsa解密数据:::", result.decode())