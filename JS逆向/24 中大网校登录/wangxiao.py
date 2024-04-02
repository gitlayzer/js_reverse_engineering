# coding: utf-8
"""
@python version : python3.10
@file name      : wangxiao.py
@date           : 2024/4/2 13:36
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests
import base64
import json
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

session = requests.session()

session.get("https://user.wangxiao.cn/login")
session.headers['Content-Type'] = "application/json;charset=UTF-8"

# (1) 获取验证码
url = "https://user.wangxiao.cn/apis//common/getImageCaptcha"
res = session.post(url)
img_data = res.json().get("data").split(",")[-1]
with open("validCode.png", "wb") as f:
    f.write(base64.b64decode(img_data))


# (2) 基于打码平台实现验证码识别
def base64_api(b64):
    data = {"username": "q6035945", "password": "q6035945", "typeid": 3, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


code = base64_api(img_data)
print(code)

# (3) 逆向password数据
res = session.post("https://user.wangxiao.cn/apis//common/getTime")
# timestamp = res.json().get("data")
# print(timestamp)
timestamp = str(int(time.time() * 1000))
print(timestamp)
publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"
rsa_pk = RSA.importKey(base64.b64decode(publicKey))
rsa = PKCS1_v1_5.new(rsa_pk)

user = "13121758648"
pwd = "13121758648yuan"
data = pwd + timestamp
encrypt_data = rsa.encrypt(data.encode())
# print("encrypt_data:::",encrypt_data)
pwd_enc = base64.b64encode(encrypt_data).decode()
print(pwd_enc)

# (4) 模拟请求
url = "https://user.wangxiao.cn/apis//login/passwordLogin"

data = {
    "imageCaptchaCode": code,
    "userName": "13121758648",
    "password": pwd_enc
}

res = session.post(url, data=json.dumps(data))
print("res:::", res.text)

login_success_data = res.json().get("data")

# 写cookie
session.cookies['autoLogin'] = 'null'
session.cookies['userInfo'] = json.dumps(login_success_data)  # 这里可以先放着. 如果请求数据不成功. 可以考虑添加urlencode(quote/quote_plus)
session.cookies['token'] = login_success_data.get("token")

session.cookies['UserCookieName'] = login_success_data.get("userName")
session.cookies['OldUsername2'] = login_success_data.get("userNameCookies")
session.cookies['OldUsername'] = login_success_data.get("userNameCookies")
session.cookies['OldPassword'] = login_success_data.get("passwordCookies")
session.cookies['UserCookieName_'] = login_success_data.get("userName")
session.cookies['OldUsername2_'] = login_success_data.get("userNameCookies")
session.cookies['OldUsername_'] = login_success_data.get("userNameCookies")
session.cookies['OldPassword_'] = login_success_data.get("passwordCookies")
session.cookies[login_success_data.get('userName') + "_exam"] = login_success_data.get("sign")

# 二、拓展请求：获取该网站数据
url = "http://ks.wangxiao.cn/practice/listQuestions"
data = {
    "practiceType": "2",
    "sign": "jz2",
    "subsign": "467b39463bc6cbc2e7d6",
    "examPointType": "",
    "questionType": "",
    "top": "30"}

print(session.cookies.get_dict())
res = session.post(url, data=json.dumps(data))
print(res.text)
