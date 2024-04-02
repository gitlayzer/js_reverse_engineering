# coding: utf-8
"""
@python version : python3.10
@file name      : main.py
@date           : 2024/4/2 10:59
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import json
import execjs
import requests
import base64

# 获取登录验证码
session = requests.session()
session.get('https://user.wangxiao.cn/login')
# cookies = {
#     'sessionId': '1712025134545',
#     'mantis6894': '28380e35a7ea461b922f932f3c839361@6894',
#     'Hm_lvt_86efc728d941baa56ce968a5ad7bae5f': '1712025136',
#     '_bl_uid': '29lqLu4yhRarpakav9gXdp77apOC',
#     'Hm_lpvt_86efc728d941baa56ce968a5ad7bae5f': '1712026223',
# }

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'sessionId=1712025134545; mantis6894=28380e35a7ea461b922f932f3c839361@6894; Hm_lvt_86efc728d941baa56ce968a5ad7bae5f=1712025136; _bl_uid=29lqLu4yhRarpakav9gXdp77apOC; Hm_lpvt_86efc728d941baa56ce968a5ad7bae5f=1712026223',
    'EagleEye-SessionID': '2kl9CuR9hqzs9a7qhkatej3oqtCR',
    'EagleEye-TraceID': '4f894a771712026251582101081d1d',
    'EagleEye-pAppName': 'ihuy5j2ab7@7cd9bc63da81d1d',
    'Origin': 'https://user.wangxiao.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://user.wangxiao.cn/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sessionId': '1712025134545',
    'source': 'pc',
    'token': '',
}

response = session.post('https://user.wangxiao.cn/apis//common/getImageCaptcha', headers=headers)
b64_code = response.json().get('data').split(',')[-1]  # 获取验证码图片base64编码
# 解码，写入本地
with open('code.png', 'wb') as f:
    content = base64.b64decode(b64_code)
    f.write(content)


# 打码平台识别验证码
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

## 登录请求
username = '18761661318'
password = 'yang///1318'
# 执行js获取加密密码
encrypt_pwd = execjs.compile(open('1.js', 'r', encoding='utf-8').read()).call('decrypt_pwd', password)
# 构建请求体数据
data = {
    'userName': username,
    'imageCaptchaCode': code_str,
    'password': encrypt_pwd,
}
# 因为请求头是  'Content-Type': 'application/json;charset=UTF-8', 需要把data转换成json
login_res=session.post('https://user.wangxiao.cn/apis//login/passwordLogin', headers=headers, data=json.dumps(data))
print(login_res.text)
# {"code":0,"msg":"成功","data":{"userName":"pc_818594229","token":"55cded29-8971-4831-add5-951cf9a31fb9","headImg":null,"nickName":"187****1318","sign":"fangchan","isBindingMobile":"1","isSubPa":"0","userNameCookies":"+RWefRJN/AO42UAlo3lMdw==","passwordCookies":"vtN4tFw3qFe2bjVbvXevkw=="},"operation_date":"2024-04-02 11:51:49"}