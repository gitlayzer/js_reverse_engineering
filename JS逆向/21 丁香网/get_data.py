import json
import time

import requests
import execjs
cookies = {
    'dxy_da_cookie-id': 'd6f1e1d712f27be0ac62824fad669ac11711777905350',
    '_ga': 'GA1.1.284808802.1711777905',
    'JUTE_SESSION_ID': '41a4cf00-e1c0-41eb-ab9f-781b575a7186',
    'ifVisitOldVerBBS': 'false',
    'Hm_lvt_5fee00bcc4c092fe5331cc51446d8be2': '1711777906,1711803618,1711811421,1711858596',
    'Hm_lpvt_5fee00bcc4c092fe5331cc51446d8be2': '1711858596',
    '_ga_LTBPLJJK75': 'GS1.1.1711858595.4.0.1711858595.0.0.0',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=utf-8',
    # 'cookie': 'dxy_da_cookie-id=d6f1e1d712f27be0ac62824fad669ac11711777905350; _ga=GA1.1.284808802.1711777905; JUTE_SESSION_ID=41a4cf00-e1c0-41eb-ab9f-781b575a7186; ifVisitOldVerBBS=false; Hm_lvt_5fee00bcc4c092fe5331cc51446d8be2=1711777906,1711803618,1711811421,1711858596; Hm_lpvt_5fee00bcc4c092fe5331cc51446d8be2=1711858596; _ga_LTBPLJJK75=GS1.1.1711858595.4.0.1711858595.0.0.0',
    'referer': 'https://www.dxy.cn/bbs/newweb/pc/case',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

data = execjs.compile(open('mod.js','r',encoding='utf-8').read()).call('get_data')

svc_params = {
    'serverTimestamp': '0',
    'timestamp': str(data['timestamp']),
    'noncestr': str(data['noncestr']),
    'sign': data['sign'],
}
svc_url = 'https://www.dxy.cn/bbs/newweb/sys/time-millis/info'
svc_res = requests.get(svc_url,params=svc_params,cookies=cookies,headers=headers)
server_time = json.loads(svc_res.text)['data']
data2 = execjs.compile(open('mod.js','r',encoding='utf-8').read()).call('get_data')

timeStamp = int(time.time()*1000)
params = {
    'sectionCode': '0',
    'pageSize': '10',
    'pageNum': '1',
    'serverTimestamp': timeStamp-2,
    'timestamp': timeStamp,
    'noncestr': '61359818',
}
f = f"appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&noncestr=59030781&serverTimestamp={server_time}&timestamp={str(int(time.time())*1000)}"

#s1 = f'appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&keyword={params["keyword"]}&noncestr={params["noncestr"]}&pageNum={params["pageNum"]}&pageSize={params["pageSize"]}&sectionCode=0&serverTimestamp={params["serverTimestamp"]}&timestamp={params["timestamp"]}'
s = f"appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&noncestr=61359818&pageNum=1&pageSize=10&sectionCode=0&serverTimestamp={timeStamp-2}&timestamp={timeStamp}"
# print(s1)
print(s)
sign = execjs.compile(open('1.js','r',encoding='utf-8').read()).call('get_sign',s)
params['sign'] = sign
response = requests.get('https://www.dxy.cn/bbs/newweb/case-bank/page-post-info', params=params, cookies=cookies, headers=headers)
print(response.text)