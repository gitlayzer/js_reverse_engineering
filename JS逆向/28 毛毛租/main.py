# coding: utf-8
# https://www.maomaozu.com/#/build
import json

import requests
import time
import execjs

from Crypto.Cipher import AES
import base64
cookies = {
    'PHPSESSID': 'aksse1lv3lue6044h9hbru44sn',
    'Hm_lvt_6cd598ca665714ffcd8aca3aafc5e0dc': '1712233353',
    'Hm_lpvt_6cd598ca665714ffcd8aca3aafc5e0dc': '1712233381',
    'SECKEY_ABVK': 'zGUu2QLUJ7qRYXVp1elfDI8pwGDPW+7h04g/MSL07zo%3D',
    'BMAP_SECKEY': 'Iy_JbRwXGhsSlB87WvuFRg86E2UCVqMDHdgLfsoW4QJnLyeEUB80NSnghqEy_s064W7BNWHDj1oUTbPb_fC216LUw2wDYhaOMnBLEpgXRdM6ffrJEBAzJamhTcoVNNX4AQSNqTy6ahmDVp-1cC10KrDSPGgpS9D-oz_kTYv6aKV1cMTNYjoNRAXwU7e-hOsE',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=aksse1lv3lue6044h9hbru44sn; Hm_lvt_6cd598ca665714ffcd8aca3aafc5e0dc=1712233353; Hm_lpvt_6cd598ca665714ffcd8aca3aafc5e0dc=1712233381; SECKEY_ABVK=zGUu2QLUJ7qRYXVp1elfDI8pwGDPW+7h04g/MSL07zo%3D; BMAP_SECKEY=Iy_JbRwXGhsSlB87WvuFRg86E2UCVqMDHdgLfsoW4QJnLyeEUB80NSnghqEy_s064W7BNWHDj1oUTbPb_fC216LUw2wDYhaOMnBLEpgXRdM6ffrJEBAzJamhTcoVNNX4AQSNqTy6ahmDVp-1cC10KrDSPGgpS9D-oz_kTYv6aKV1cMTNYjoNRAXwU7e-hOsE',
    'Origin': 'https://www.maomaozu.com',
    'Referer': 'https://www.maomaozu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {"Type": 0, "page": 3, "expire": int(time.time()) * 1000}
JS = execjs.compile(open('js.js', 'r', encoding='utf-8').read())
# 获取加密请求体数据
data = JS.call('encrypt', json.dumps(params))

response = requests.post('https://www.maomaozu.com/index/build.json', cookies=cookies, headers=headers, data=data)

# 解密响应数据
# 解码
aes = AES.new(b'0a1fea31626b3b55',AES.MODE_CBC,b'0a1fea31626b3b55')
plain_data = aes.decrypt(base64.b64decode(response.text.encode())).decode()
print(plain_data)
