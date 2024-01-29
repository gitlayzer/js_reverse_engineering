# coding: utf-8
"""

from: zh
to: en
query: 再见
simple_means_flag: 3
sign: 232216.485417
token: 432967fc774d1454748e3941b3a1afcd
domain: common
ts: 1706495629056


from: zh
to: en
query: 你好
simple_means_flag: 3
sign: 232427.485594
token: 432967fc774d1454748e3941b3a1afcd
domain: common
ts: 170649555446
"""
import sys

import requests
import execjs
import time

cookies = {
    'BIDUPSID': '8CA51CC5DE327A236B18BE71885F8E4E',
    'PSTM': '1676254428',
    'BAIDUID': '8CA51CC5DE327A238B4297A16429C4EB:FG=1',
    'BDUSS': 'UxSEREQXhHekxYaE9uTE9MY2I2d21tUjJGZXZEflc3RTN0Nktibnd-ZVBlMHhrSVFBQUFBJCQAAAAAAAAAAAEAAADapxoNbWFpZGkxNDc4NTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI~uJGSP7iRkVV',
    'BDUSS_BFESS': 'UxSEREQXhHekxYaE9uTE9MY2I2d21tUjJGZXZEflc3RTN0Nktibnd-ZVBlMHhrSVFBQUFBJCQAAAAAAAAAAAEAAADapxoNbWFpZGkxNDc4NTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI~uJGSP7iRkVV',
    'MCITY': '-289%3A',
    'H_WISE_SIDS_BFESS': '40019_40044',
    'H_PS_PSSID': '40019_40044_39996',
    'H_WISE_SIDS': '40019_40044_39996',
    'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
    'REALTIME_TRANS_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'BAIDUID_BFESS': '8CA51CC5DE327A238B4297A16429C4EB:FG=1',
    'PSINO': '5',
    'BA_HECTOR': '20048g0g248000a52k00a48gclv7bd1ire5ma1s',
    'ZFY': 'xRJX1lfNhf8XtGdA:BLSjbH2W5kCWINJ55btyG:AE32ck:C',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1706494585,1706497745',
    'APPGUIDE_10_6_9': '1',
    'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1706499682',
    'ab_sr': '1.0.1_YzI4NjEwNTE3MTRlNjhhZTIyNjFjYjE1ZTg1NGJkZjhmZDg0NDM4NjdmYzA3Nzk0N2YyODdjMWE2YzExMTcwM2MzYjhjZWM5ODI1MjNhYTBmMjM3ODFkYmY0MWEwYWNjZWEyN2NlZjZlYzFiZDI1OGUzYTlhMGM2YWY4ZmY4MmM2YTIyZDU2YjkyMjI1NzkwZDE1YzQxNWMxZTNiNGY1ODcwMDk3NDY3YjU1OGIxMDNjZjE5MWZkNGM4NzZhYjA0',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1706439979902_1706500055686_z7KFYs24lZyOo6S6Fsu+KLblDUQAOmQ7JyPBjJLoEnkP+X7l3VIVGa0zBvG3PdxhC3PDEkUB5sk0pZMCHSiC98hKXNR9irBTdMlSl4Ddex/bUgTlcQOnafE+DQH+Day0jUIihPDC3+P8xWKXjJ3S8VBrPdyN/NralBLEDdgocYhb17uXX4q/FFzBs0eynAIAl+IwH5wvS34RTa0L1FwcmsaOiFr9eVq8Wa+/OhbUm4B0fjxIta0oAyhRj19tOeZKGJbdK1qAOHbQ1+YheS02lfpesr5gbooc2OrAF/2UsW/86ZUj+UVraz+M+wOUdplGgDzx9khVgOjy88DGmWZrwaZ8ItoOPjWB+DkohzbmnlKTn1zyffo0uM62pgdei42P+HAuJdgau7qQsU9jg6XA++HWXGsMvJCaN77HfX1ZMDYfZxUGNvOSGkXc2x2m/U9jdLBwVUk6D+uxqrK3+3ZHnynwmDM952wD+rQLiO8o16k=',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'BIDUPSID=8CA51CC5DE327A236B18BE71885F8E4E; PSTM=1676254428; BAIDUID=8CA51CC5DE327A238B4297A16429C4EB:FG=1; BDUSS=UxSEREQXhHekxYaE9uTE9MY2I2d21tUjJGZXZEflc3RTN0Nktibnd-ZVBlMHhrSVFBQUFBJCQAAAAAAAAAAAEAAADapxoNbWFpZGkxNDc4NTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI~uJGSP7iRkVV; BDUSS_BFESS=UxSEREQXhHekxYaE9uTE9MY2I2d21tUjJGZXZEflc3RTN0Nktibnd-ZVBlMHhrSVFBQUFBJCQAAAAAAAAAAAEAAADapxoNbWFpZGkxNDc4NTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI~uJGSP7iRkVV; MCITY=-289%3A; H_WISE_SIDS_BFESS=40019_40044; H_PS_PSSID=40019_40044_39996; H_WISE_SIDS=40019_40044_39996; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID_BFESS=8CA51CC5DE327A238B4297A16429C4EB:FG=1; PSINO=5; BA_HECTOR=20048g0g248000a52k00a48gclv7bd1ire5ma1s; ZFY=xRJX1lfNhf8XtGdA:BLSjbH2W5kCWINJ55btyG:AE32ck:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1706494585,1706497745; APPGUIDE_10_6_9=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1706499682; ab_sr=1.0.1_YzI4NjEwNTE3MTRlNjhhZTIyNjFjYjE1ZTg1NGJkZjhmZDg0NDM4NjdmYzA3Nzk0N2YyODdjMWE2YzExMTcwM2MzYjhjZWM5ODI1MjNhYTBmMjM3ODFkYmY0MWEwYWNjZWEyN2NlZjZlYzFiZDI1OGUzYTlhMGM2YWY4ZmY4MmM2YTIyZDU2YjkyMjI1NzkwZDE1YzQxNWMxZTNiNGY1ODcwMDk3NDY3YjU1OGIxMDNjZjE5MWZkNGM4NzZhYjA0',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'from': 'zh',
    'to': 'en',
}

with open('fanyi.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
key_word = sys.argv[1]
sign = execjs.compile(js_code).call('get_sign', key_word)


data = {
    'from': 'zh',
    'to': 'en',
    'transtype': 'realtime',
    'query': key_word,
    'simple_means_flag': '3',
    'sign': sign,
    'token': '432967fc774d1454748e3941b3a1afcd',
    'domain': 'common',
    'ts': time.time(),
}
response = requests.post('https://fanyi.baidu.com/v2transapi', params=params, cookies=cookies, headers=headers,
                         data=data)

# print(response.json())
print(response.json()['trans_result']['data'][0]['dst'])
