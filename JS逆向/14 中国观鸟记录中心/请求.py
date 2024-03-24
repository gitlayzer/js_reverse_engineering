import execjs
import requests
from urllib.parse import urlencode


def start():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    with open('1.js') as f:
        js_code = f.read()
    js = execjs.compile(js_code)
    data = {
        "limit": "20",
        "page": "1",
    }
    encoded = urlencode(data)
    print('编码后的数据', encoded)
    sign_data = js.call("get_headers", encoded)
    print("sign_data:::", sign_data['data'])
    headers.update(sign_data['headers'])
    print("headers:::", headers)
    url = 'https://api.birdreport.cn/front/activity/search'
    res = requests.post(url, headers=headers, data=sign_data['data'])
    data = res.json()
    print(data)


if __name__ == '__main__':
    print(start())

