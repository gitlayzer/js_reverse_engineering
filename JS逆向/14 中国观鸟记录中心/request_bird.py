# coding: utf-8
"""
@python version : python3.10
@file name      : request_bird.py
@date           : 2024/3/25 13:53
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

from urllib.parse import urlencode
import requests
import time
import execjs
import json
from hashlib import md5


# 获取 headers 三个参数 和 data
def get_info():
    # 构造明文数据字典
    data_dict = {"limit": "20", "page": "1"}  # 第几页，每页多少行
    # 进行url编码
    data_url_str = urlencode(data_dict)
    with open('get_info.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    js_obj = execjs.compile(js_code)
    info = js_obj.call('getInfo', data_url_str)
    request_id = info['request_id']
    data = info['data']
    e = info['e']
    t = str(int(time.time()) * 1000)
    sign = get_sign(e, request_id, t)
    return request_id, sign, t, data


def get_sign(e, d, t):
    """
    :param e: json序列化之后的请求体数据
    :param d: requestId
    :param t: 时间戳
    :return:
    """
    m = md5()
    m.update(f"{e}{d}{t}".encode())
    sign = m.hexdigest()
    return sign


# 获取headers 和请求体数据
def get_headers_data():
    request_id, sign, t, data = get_info()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Requestid': request_id,
        'Referer': 'http://pms.birdreport.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Sign': sign,
        'Timestamp': t,
    }

    return headers, data


# 获取加密数据
def get_response_data():
    url = 'https://api.birdreport.cn/front/activity/search'
    headers, data = get_headers_data()
    response = requests.post(url=url, headers=headers, data=data)
    res_data = json.loads(response.content)
    return res_data


# 获取解密后响应的数据
def get_decrypt_data():
    encrypt_data = get_response_data()['data']
    with open('decrypt.js', 'r', encoding='utf-8') as f:
        jsCode = f.read()
    plain_data = execjs.compile(jsCode).call('decrypt', encrypt_data)
    return plain_data


if __name__ == '__main__':
    decrypt_data = get_decrypt_data()
    print(decrypt_data)
