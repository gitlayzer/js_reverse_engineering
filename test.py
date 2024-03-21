# coding: utf-8
"""
@python version : python3.10
@file name      : test.py
@date           : 2024/3/18 11:46
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import requests

res = requests.get('https://devops.psi-gene.com/api/app/')
print(res.text)