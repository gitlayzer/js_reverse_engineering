# coding: utf-8
import requests
import execjs
cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1706592723',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1706597116',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1706592723; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1706597116',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'accessToken': '',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
    'v': '231012',
}

params = {
    'pg': '2',
    'pgsz': '15',
    'total': '450',
}

response = requests.get(
    'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list',
    params=params,
    cookies=cookies,
    headers=headers,
)
data = response.text
with open('c.js', 'r', encoding='UTF-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode).call('b', data)
print(ctx)