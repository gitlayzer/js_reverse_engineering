# coding: utf-8
"""
@python version : python3.10
@file name      : gate_data.py
@date           : 2024/4/1 10:56
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

import requests
import execjs

cookies = {
    'Hm_lvt_6088e7f72f5a363447d4bafe03026db8': '1711933610',
    'Hm_lpvt_6088e7f72f5a363447d4bafe03026db8': '1711940143',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_6088e7f72f5a363447d4bafe03026db8=1711933610; Hm_lpvt_6088e7f72f5a363447d4bafe03026db8=1711940143',
    'Origin': 'https://www.aqistudy.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.aqistudy.cn/html/city_realtime.php?v=2.3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {'hXhY1B2Kd': execjs.compile(open('1.js', 'r', encoding='utf-8').read()).call('get_params', 'GETDATA', {'city':'济南'})}
response = requests.post('https://www.aqistudy.cn/apinew/aqistudyapi.php', cookies=cookies, headers=headers, data=data)
encrypt_data = response.text
plain_data = execjs.compile(open('1.js', 'r', encoding='utf-8').read()).call('deIZLF7oahc0DLiXbqt',encrypt_data)
print(plain_data)
