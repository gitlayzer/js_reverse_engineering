import requests
import execjs
import random
import time

cookies = {
    'dxy_da_cookie-id': '5e6a2e85b2e9e74837bebc361549bf4d1702294707030',
    'ifVisitOldVerBBS': 'false',
    '_ga': 'GA1.1.168654756.1702294708',
    'Hm_lvt_5fee00bcc4c092fe5331cc51446d8be2': '1702294707,1702723305,1703862131,1704529575',
    'JUTE_SESSION_ID': '511f03e5-9ea5-4c43-b305-1cb75ea1fc50',
    'Hm_lpvt_5fee00bcc4c092fe5331cc51446d8be2': '1704716217',
    '_ga_LTBPLJJK75': 'GS1.1.1704716192.13.1.1704716217.0.0.0',
}

headers = {
    'authority': 'www.dxy.cn',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=utf-8',
    # 'cookie': 'dxy_da_cookie-id=5e6a2e85b2e9e74837bebc361549bf4d1702294707030; ifVisitOldVerBBS=false; _ga=GA1.1.168654756.1702294708; Hm_lvt_5fee00bcc4c092fe5331cc51446d8be2=1702294707,1702723305,1703862131,1704529575; JUTE_SESSION_ID=511f03e5-9ea5-4c43-b305-1cb75ea1fc50; Hm_lpvt_5fee00bcc4c092fe5331cc51446d8be2=1704716217; _ga_LTBPLJJK75=GS1.1.1704716192.13.1.1704716217.0.0.0',
    'referer': 'https://www.dxy.cn/bbs/newweb/pc/case/search?keyword=%E6%96%B0%E5%86%A0',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '11d5d86d65824b76a5c8dc79fc6977b5-8d43ac2155997d66-1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

nonstr = str(random.randint(0, 100000000)).rjust(8, '0')
# nonstr = ''.join([str(random.randint(0, 9)) for _ in range(8)])
timestamp = int(time.time() * 1000)

params = {
    'keyword': '新冠',
    'sectionCode': '0',
    'pageSize': '10',
    'pageNum': '1',
    'serverTimestamp': timestamp-2,
    'timestamp': timestamp,
    'noncestr': nonstr,
}

data = f'appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&keyword={params["keyword"]}&noncestr={params["noncestr"]}&pageNum={params["pageNum"]}&pageSize={params["pageSize"]}&sectionCode=0&serverTimestamp={params["serverTimestamp"]}&timestamp={params["timestamp"]}'
sign = execjs.compile(open("02 丁香网.js").read()).call("u", data)
print("sign", sign)
params["sign"] = sign

response = requests.get('https://www.dxy.cn/bbs/newweb/case-bank/page-post-info', params=params, cookies=cookies,
                        headers=headers)

print(response.text)
