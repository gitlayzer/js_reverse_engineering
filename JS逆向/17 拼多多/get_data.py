# coding: utf-8
"""
@python version : python3.10
@file name      : get_data.py
@date           : 2024/3/28 11:20
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import execjs
import requests
anti_content = execjs.compile(open('pdd.js','r',encoding='utf-8').read()).call('get_anti_content')
print(anti_content)

url = 'https://apiv2.pinduoduo.com/api/gindex/tf/query_tf_goods_info'

params = {
    'tf_id': 'TFRQ0v00000Y_13396',
    'page': '1',
    'size': '100',
    'anti_content': anti_content
}
headers = {
    'Accept': 'application/json, text/javascript',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.pinduoduo.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.pinduoduo.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',

}
res = requests.get(url=url, params=params, headers=headers)
print(res.text)
