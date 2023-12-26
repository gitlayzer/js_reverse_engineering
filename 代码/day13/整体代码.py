# @课程    : 爬虫逆向实战课
# @讲师    : 武沛齐
# @课件获取 : wupeiqi666
import json
import random
import time
import base64
import binascii

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import json
import random
import time
import base64
import binascii

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import random
import string
import time
import binascii
import hmac
from hashlib import sha1
from urllib.parse import quote_plus


def hmac_sha1(data_string):
    key_string = "68386673614b337771652b696f4d7673"
    key = binascii.a2b_hex(key_string)
    # data_string = '40450e94c5aa344460ef3363f0cabffe7fOOyzy-rotp_WORtvsxe["slideToken"]'
    hmac_code = hmac.new(key, data_string.encode("utf-8"), sha1)
    return hmac_code.hexdigest()


def _0x26cf34(_0x4800e6, _0x572efb):
    _0x5ee954 = ['qunar', 'tujia']
    _0x403118 = "B6F1YrNm+OA=sw"
    _0x501116 = "n8xbeLlzQ"
    _0x3b5454 = "p5M02SUHt/dog"
    _0x251b31 = "cyfj-9kPKu"
    _0x222d7d = "EX7VWaqJi"
    _0x47c310 = "3CIGDRhTv4"

    _0x3af887 = "".join(_0x572efb) + (_0x403118 + _0x501116 + _0x3b5454 + _0x251b31 + _0x222d7d + _0x47c310)
    _0x3af887 = list(_0x403118 + _0x501116 + _0x3b5454 + _0x251b31 + _0x222d7d + _0x47c310)

    _0x4800e6 = quote_plus(_0x4800e6)
    while len(_0x4800e6) % 0x3 != 0x0:
        _0x4800e6 += '\x20'

    _0x933810 = [format(ord(i), "0>8b") for i in _0x4800e6]

    _0x2e4d85 = []
    for i in range(0, len(_0x933810), 3):
        end_index = min(i + 3, len(_0x933810))
        group = _0x933810[i:end_index]
        _0x2e4d85.append(group)

    _0x2a779b = ''
    for _0x28ee6c in _0x2e4d85:
        _0x572061 = "".join(_0x28ee6c)
        _0x351bb8 = []
        for j in range(0, len(_0x572061), 6):
            end_idx = min(j + 6, len(_0x572061))
            _0x351bb8.append(_0x572061[j:end_idx])

        new_0x351bb8 = []
        for _0x2a9721 in _0x351bb8:
            _0x2a9721 = "".join(["0" if char == "1" else "1" for char in _0x2a9721])
            idx = int(_0x2a9721, base=2)
            part = _0x3af887[idx]
            new_0x351bb8.append(part)

        _0x2a779b += "".join(new_0x351bb8)
    return _0x2a779b


def get_bella(slide_token):
    # slide_token = "15cf502c3128593b1a3237e5c484d6c9"

    _0x4dd553 = {"keyArray": ["slideToken"], "bParam": slide_token}

    total_string = string.digits + string.ascii_letters
    random_string = "".join([random.choice(total_string) for _ in range(16)])

    _0x4fb8ac = {
        "referer": "",
        "piccolo": f"{random.randint(1000, 9999)}##{random_string}##{int(time.time() * 1000)}",
        "shirley": "unknown",
        "title": "unknown",
        "keywords": "unknown",
        "description": "unknown",
        "host": "user.qunar.com",
        "scriptSrc": ["qimgs.qunarzz.co", "q.qunarzz.com/ho"]
    }

    total_string = "-_zyxwvutsrqponmlkjihgfedcba9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA"
    _0x34877a = "".join([random.choice(total_string) for _ in range(21)])

    _0x5ad2bb = slide_token + _0x34877a + json.dumps(_0x4dd553['keyArray'])

    _0xc21476 = hmac_sha1(_0x5ad2bb)

    _0x4fb8ac["sign"] = _0xc21476
    _0x4fb8ac["randomNum"] = _0x34877a
    _0x4fb8ac['t'] = int(time.time() * 1000)

    _0x572efb = ["B6F1YrNm+OA=sw", "n8xbeLlzQ", "p5M02SUHt/dog", "cyfj-9kPKu", "EX7VWaqJi", "3CIGDRhTv4"]
    _0x34c54c = _0x26cf34(json.dumps(_0x4fb8ac, separators=(',', ':')), _0x572efb)

    june_v = '1683616182042'
    _0x112026 = june_v + '##' + _0xc21476 + '##' + _0x34c54c + '##' + _0x34877a + '##' + "slideToken"
    return _0x112026


def get_slider_list():
    slider_list = []
    client_x = 300
    client_y = 500
    start_time = int(int(time.time() * 1000) % 1e5)
    width = random.randint(419, 431)
    for slice_distance in range(3, width, 26):
        if width - slice_distance <= 26:
            slice_distance = width
        start_time += random.randint(10, 1000)
        i = start_time
        o = f"{client_x + slice_distance}.00"
        u = f"{client_y + random.randint(-5, 5)}.00"
        a = f"{slice_distance}.00"
        f = f"{i};{o};{u};{a}"
        slider_list.append(f)
    return slider_list


def aes_encrypt(data_string):
    # key = "227V2xYeHTARSh1R".encode('utf-8')
    key_string = "32323756327859654854415253683152"
    key = binascii.a2b_hex(key_string)

    aes = AES.new(
        key=key,
        mode=AES.MODE_ECB
    )
    raw = pad(data_string.encode('utf-8'), 16)
    aes_bytes = aes.encrypt(raw)
    res_string = base64.b64encode(aes_bytes).decode('utf-8')
    return res_string


def run():
    mobile = input("请输入手机号：")

    res = requests.get("https://user.qunar.com/passport/login.jsp")
    cookie_dict = res.cookies.get_dict()
    cookie_qn1 = cookie_dict['QN1']

    slider_list = get_slider_list()
    slider_info = {
        "openTime": int((time.time() - random.randint(500, 3000)) * 1000),
        "startTime": int((time.time() - random.uniform(2, 4)) * 1000),
        "endTime": int((time.time() - random.uniform(0, 1)) * 1000),
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "uid": cookie_qn1,
        "track": slider_list,
        "acc": [],
        "ori": [],
        "deviceMotion": [{"isTrusted": True} for _ in range(random.randint(10, 100))]
    }

    data_string = json.dumps(slider_info, separators=(',', ':'))
    data = aes_encrypt(data_string)
    res = requests.post(
        url="https://vercode.qunar.com/inner/captcha/snapshot",
        json={
            "appCode": "register_pc",
            "cs": "pc",
            "data": data,
            "orca": 2
        },
        cookies=cookie_dict
    )
    res_dict = res.json()
    slide_token = res_dict['data']["cst"]
    cookie_dict.update(res.cookies.get_dict())

    # import subprocess
    # res = subprocess.check_output(f'node v1.js "{slide_token}"', shell=True)
    # bella_string = res.decode('utf-8').strip()
    bella_string = get_bella(slide_token)

    res = requests.post(
        url="https://user.qunar.com/weblogin/sendLoginCode",
        data={
            "usersource": "",
            "source": "",
            "ret": "",
            "ref": "",
            "business": "",
            "pid": "",
            "originChannel": "",
            "activityCode": "",
            "origin": "",
            "mobile": mobile,
            "prenum": "86",
            "loginSource": "1",
            "slideToken": slide_token,
            "smsType": "0",
            "appcode": "register_pc",
            "bella": bella_string,
            "captchaType": ""
        },
        cookies=cookie_dict
    )
    print(res.text)
    cookie_dict.update(res.cookies.get_dict())

    sms_code = input("请输入短信验证码：")
    res = requests.post(
        url="https://user.qunar.com/weblogin/verifyMobileVcode",
        json={
            "piccoloT": "login_register_pc",
            "mobile": mobile,
            "prenum": "86",
            "vcode": sms_code,
            "type": "3",
            "slideToken": slide_token,
            "appcode": "register_pc",
            "loginSource": 1,
            "captchaType": "",
            "source": "",
            "usersource": "",
            "ret": "",
            "ref": "",
            "business": "",
            "pid": "",
            "originChannel": "",
            "activityCode": ""
        }
    )
    cookie_dict.update(res.cookies.get_dict())

    print(res.text)
    print(cookie_dict)


if __name__ == '__main__':
    run()