# coding: utf-8
"""
@python version : python3.10
@file name      : 初识bs4.py
@date           : 2024/3/12 15:53
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from bs4 import BeautifulSoup

with open(r'C:\Users\杨子洋\PycharmProjects\JS逆向\03 正则\250.html','r',encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data,'html.parser')
# 查询所有的a标签
a =soup.find_all("a")
# 获取a标签下得href属性值
# for link in a:
#     print(link.get("href"))
print(soup.a)