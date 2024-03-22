# coding: utf-8
"""
@python version : python3.10
@file name      : 基于python解密数据.py
@date           : 2024/3/22 15:38
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

import base64
import json
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

base64_data = "Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6JKK7ArS9fJXAcsG7ufBIE0gd6fbnhFcsGmdXspZe-8whVFbRB_8Fc9JlMHh8DDXnskDhGfEscN_rfi-A-AHB3F9Vets82vIYpkGNaJOft_JA-m5cGEjo-UNRDDpkTz_NIAvo5PbATpkh7PSna2tHcE6Hou9GBtPLB67vjScwplB96-zqZKXJJEzU5HGF0oPDY_weAkXArzXyGLBPXFCnn_IWJDkGD4vqBQQAh2n52f48GD_cb-PSCT_8b-ESsKUI9NJa11XsdaUZxAc8TzrYnXwdcQbtl_kZGKhS6_rCtuNEBouA_lvM2CbS7TTtV2U4zVmJKpp-c6nt3yZePK3Av01GWn1pH_3sZbaPEx8DUjSbdp4i4iK-Mj4p2HPoph67DR7B9MFETYku_28SgP9xsKRRvFH4aHBHESWX4FDbwaU="
# 上述是base64变种，需要对格式化，形成标准的base54编码

# 1.解码,获取加密数据
encrypt_data = base64.b64decode(base64_data.encode(), altchars='-_')

# 2. 获取key,iv
key_str = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
iv_str = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'


def to_md5(s):
    m = md5()
    m.update(s.encode())
    return m.digest()


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
print(t_res)
