# coding: utf-8
"""
@python version : python3.10
@file name      : 有道翻译完整版基于py解密.py
@date           : 2024/3/22 16:47
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests
import time
import base64
import json
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


# 获取session对象
def get_session():
    session = requests.session()
    session.get('https://fanyi.youdao.com/index.html#/')

    return session


# 获取加密并编码的响应数据
def get_encrypt_data(input_word):
    session = get_session()
    key = "fsdsogkndfokasodnaso"  # 固定值
    mysticTime = str(int(time.time()) * 1000)
    s = f'client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key={key}'
    md5_obj = md5(s.encode())
    sign = md5_obj.hexdigest()
    data = {
        "i": input_word,
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


def to_md5(s):
    m = md5()
    m.update(s.encode())
    return m.digest()


# 解密并解码数据
def decrypt_decode_data(input_word):
    # 1.解码,获取加密数据
    response_data = get_encrypt_data(input_word)
    encrypt_data = base64.b64decode(response_data.encode(), altchars='-_')

    # 2. 获取key,iv
    key_str = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
    iv_str = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
    key = to_md5(key_str)
    iv = to_md5(iv_str)

    # 2. 解密数据

    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypt_data_byte = aes.decrypt(encrypt_data)
    # 对解密的数据去除填充
    decrypt_data = unpad(decrypt_data_byte, 16)
    decrypt_dict = json.loads(decrypt_data.decode())
    # 获取翻译结果

    translate_result = decrypt_dict['translateResult'][0]  # 获取所有的翻译结果
    t_res = '\n'.join([item['tgt'] for item in translate_result])
    return t_res


def translate(word_str):
    result = decrypt_decode_data(word_str)
    print(result)
    return result


if __name__ == '__main__':
    while True:
        word = input('请输入需要翻译的内容>>>>>:')
        translate(word)
