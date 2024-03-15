# coding: utf-8
"""
@python version : python3.10
@file name      : 元字符.py
@date           : 2024/3/12 13:22
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import re

s1 = "2,f,adv,46h,5687"
res = re.findall('\d{1,3}',s1)
res2 = re.findall("[a-z]{1,2}",s1)
res3 =re.findall("\d+",s1)
print(res3)

s2="123abc@163.com,....234xyz@qq.com,...."
res4 = re.findall("\w+@(?:163|qq)\.com",s2)
print(res4)