import requests
import execjs
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.qimingpian.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'page': '2',
    'num': '20',
    'sys': 'vip',
    'keywords': '',
    'unionid': '',
}

encrypt_data = requests.post('https://vipapi.qimingpian.cn/search/recommendedItemList', headers=headers, data=data).json()['encrypt_data']

with open('data.js','r',encoding='utf-8') as f:
    js_code = f.read()
plain_data = execjs.compile(js_code).call('s',encrypt_data)
print(plain_data)
