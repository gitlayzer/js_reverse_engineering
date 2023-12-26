# coding: utf-8
import ddddocr
# 登录 https://xuexi.chinabett.com/

import requests
import re
from bs4 import BeautifulSoup
import execjs

cookie_dict = {}
res = requests.get(url="https://xuexi.chinabett.com/")
cookie_dict.update(res.cookies.get_dict())


# cookie_dict.update(res.cookies.get_dict())
# import
# 2.获取验证码地址
def get_code():
    with open('v1.js', 'r', encoding='utf-8') as f:
        js_string = f.read()

    JS = execjs.compile(js_string)
    code_url = 'https://xuexi.chinabett.com'+JS.call('letValidate', None)
    print(code_url)
    code_res = requests.get(url=code_url, cookies=cookie_dict)
    # 验证码图片识别
    ocr = ddddocr.DdddOcr(show_ad=False)
    code = ocr.classification(code_res.content)
    return code


if __name__ == '__main__':
    print(get_code())
