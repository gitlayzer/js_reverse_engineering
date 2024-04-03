# coding: utf-8
"""
@python version : python3.10
@file name      : main.py
@date           : 2024/4/3 14:15
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import json

import requests
import execjs
import base64

session = requests.session()
session.get('https://www.epwk.com/login.html')


code_url = 'https://www.epwk.com/api/epwk/v1/captcha/show'
code_data = {'channel': 'common_channel', 'base64': '1'}
code_headers = execjs.compile(open('1.js', 'r', encoding='utf-8').read()).call('getHeaders', {})
code_res = session.get(url=code_url, params=code_data, headers=code_headers)
img_base64_code = json.loads(code_res.text)['data']['base64'].replace('\r\n','')
# 将图片解码写入本地
with open('code.png','wb') as f:
    content = base64.b64decode(img_base64_code.encode())
    f.write(content)

# 通过打码平台识别验证码
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


code_str = base64_api('dittoyang', 'Yang1318', 'code.png', 3)
print(code_str)

# 拿到验证码之后进行登录
login_url = 'https://www.epwk.com/api/epwk/v1/user/login'
login_data = {
    "username": "18761661318",
    "password": "Yang///1318",
    "code": code_str,
    "hdn_refer": "https://zt.epwk.com/"
}

login_headers = execjs.compile(open('1.js', 'r', encoding='utf-8').read()).call('getHeaders', login_data)

login_res = session.post(url=login_url, data=login_data, headers=login_headers)
print(login_res.text)