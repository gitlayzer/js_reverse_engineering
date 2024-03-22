# coding: utf-8
"""
@python version : python3.10
@file name      : 有道翻译完整版基于JS代码解密数据.py
@date           : 2024/3/22 16:56
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import execjs
import requests
import time
import json
from hashlib import md5


# 获取session对象
def get_session():
    session = requests.session()
    session.get('https://fanyi.youdao.com/index.html#/')

    return session


# 获取加密并编码的响应数据
def get_encrypt_data(input_word):
    session = get_session()
    word = input_word
    key = "fsdsogkndfokasodnaso"  # 固定值
    mysticTime = str(int(time.time()) * 1000)
    s = f'client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key={key}'
    md5_obj = md5(s.encode())
    sign = md5_obj.hexdigest()
    data = {
        "i": word,
        "from": "auto",
        "to": "",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": sign,
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": mysticTime,
        "keyfrom": "fanyi.web",
        "mid": "1",
        "screen": "1",
        "model": "1",
        "network": "wifi",
        "abtest": "0",
        "yduuid": "abcdefg"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://fanyi.youdao.com/",
        "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1088350298.5964031; OUTFOX_SEARCH_USER_ID=-104466465@61.173.76.226"
    }
    res = session.post('https://dict.youdao.com/webtranslate', data=data, headers=headers)
    return res.text


def exec_js_code(word_str):
    encrypt_data = get_encrypt_data(word_str)
    with open('解密.js', 'r', encoding='utf-8') as f:
        JS_code = f.read()
    decrypt_data = execjs.compile(JS_code).call('decrypt', encrypt_data)
    decrypt_dict = json.loads(decrypt_data)
    # 获取翻译结果

    translate_result = decrypt_dict['translateResult'][0]  # 获取所有的翻译结果
    t_res = '\n'.join([item['tgt'] for item in translate_result])
    return t_res


if __name__ == '__main__':
    while True:
        word = input("请输入需要翻译的内容: ")
        tan_res = exec_js_code(word)
        print(tan_res)
