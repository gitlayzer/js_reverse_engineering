# coding: utf-8
"""
@python version : python3.10
@file name      : md5摘要算法.py
@date           : 2024/3/21 13:51
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from hashlib import md5,sha1,sha256

md5_obj = md5("def2r9 w0 mfdbeg".encode()) # 加盐处理
data = 'yzy'
md5_obj.update(data.encode())
md5_str = md5_obj.hexdigest()
print(md5_str)