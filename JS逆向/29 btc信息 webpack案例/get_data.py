# coding: utf-8
import requests
import execjs

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    'origin': 'https://mytokencap.com',
    'referer': 'https://mytokencap.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

params = {
    'pages': '1,1',
    'sizes': '100,100',
    'subject': 'market_cap',
    'language': 'zh_CN',
    'timestamp': '1712240648557',
    # 'code': '8ea5f0ee4df771005f52ad3b7e6688a6',
    'platform': 'web_pc',
    'v': '0.1.0',
    'legal_currency': 'USD',
    'international': '1',
}
with open(r'btc.js', 'r', encoding='utf-8') as f:
    JS = execjs.compile(f.read())
code = JS.call('getCode')
params['code'] = code
response = requests.get('https://api.mytokenapi.com/ticker/currencyranklist', params=params, headers=headers)
print(response.text)
