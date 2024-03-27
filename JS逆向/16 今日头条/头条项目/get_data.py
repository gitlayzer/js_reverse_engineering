# coding: utf-8
"""
@python version : python3.10
@file name      : get_data.py
@date           : 2024/3/27 15:45
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests
import execjs

url = 'https://www.toutiao.com/hot-event/hot-board/'
headers = {
    'Referer': 'https://www.toutiao.com/?wid=1711524485619',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
# 获取 get请求参数
with open('今日头条(proxy版本).js', 'r', encoding='utf-8') as f:
    JS_code = f.read()
JS = execjs.compile(JS_code)
# 获取 _signature
signature = JS.call('getSign', url)
params = {
    'origin' : 'toutiao_pc',
    '_signature' : signature
}

res = requests.get(url=url,headers=headers,params=params)
print(res.text)
