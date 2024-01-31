# coding: utf-8
import time

import requests

cookies = {
    'zhaosheng.sxu.session.id': 'cace62520d9e4b6d9a56699b50059420',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'zhaosheng.sxu.session.id=cace62520d9e4b6d9a56699b50059420',
    'Csrf-Token': '9fe739d2fd184228a17059b5c2393e0b',
    'Origin': 'https://bkzsfw.sxu.edu.cn',
    'Referer': 'https://bkzsfw.sxu.edu.cn/static/front/sxu/basic/html_web/zsjh.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Requested-Time': '1706665786530',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'ts': time.time(),
}

data = {
    'ssmc': '山西',
    'zsnf': '2023',
    'klmc': '理工',
    'zslx': '本科一批',
}

response = requests.post('https://bkzsfw.sxu.edu.cn/f/ajax_zsjh', params=params, cookies=cookies, headers=headers, data=data)
print(response.json())