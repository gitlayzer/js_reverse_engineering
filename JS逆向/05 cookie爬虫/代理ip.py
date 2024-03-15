# coding: utf-8
"""
@python version : python3.10
@file name      : 代理ip.py
@date           : 2024/3/13 10:41
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests
res = requests.get("http://httpbin.org/ip",
                   proxies={
                       "http": "114.231.8.43:8089"
                   }
                   )

print(res.text)