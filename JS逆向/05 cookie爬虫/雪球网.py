# coding: utf-8
"""
@python version : python3.10
@file name      : 雪球网.py
@date           : 2024/3/13 9:57
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

import requests
import pprint
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://xueqiu.com/",
    "Cookie": "xq_a_token=52dfb79aed5f2cdd1e7c2cfc56054ac1f5b77fc3; xqat=52dfb79aed5f2cdd1e7c2cfc56054ac1f5b77fc3; xq_r_token=e20d82fd7b432e0f32c54be5af4c28605e8c191f; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxMjM2NDQwMSwiY3RtIjoxNzEwMjk0NzIwMjE2LCJjaWQiOiJkOWQwbjRBWnVwIn0.STwYn01mVjeyMbm1CswY6WDASJw5oUQjAGZbR2o2oF7ijS30SR0a8orxCMRMzX-wMvEdtvTQedFQcBr9w0Q1sE9GWeqHNqXS6d5hHybKplreH6a3P3mDdvgXW5epaItwx9WgCz7ufCOkJyQgZXmxjoGF2Lo2LqY6IF8_0D-nUR40Z-6ZU71cIpp4JPCzkU0s9QFKh0zRX9h4jK9bjdf6EVq_bdhewWsZYzI5INTwNPFOn8KfRtbZaWJQWYn4E0hvl9yEVi35YzsHhDlaYqBhj-PKYGdnLQAWOer6Wf59jVY3_uCtCn3HVQmwqwl4NQdLy1f_GjRzqWZ95a4UmbFiGw; cookiesu=921710294753722; u=921710294753722; device_id=46f7f7f565770d2c0f41202b47c728e9; Hm_lvt_1db88642e346389874251b5a1eded6e3=1710294753; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1710294809"
}
url ='https://stock.xueqiu.com/v5/stock/batch/quote.json?symbol=SH000001,SZ399001,SZ399006,SH000688,SH000016,SH000300,BJ899050,HKHSI,HKHSCEI,HKHSTECH,.DJI,.IXIC,.INX'

res = requests.get(url=url,headers=headers)
# print(json.loads(res.content.decode()))
pprint.pprint(json.loads(res.content.decode()))