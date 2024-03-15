# coding: utf-8
"""
@python version : python3.10
@file name      : 练习.py
@date           : 2024/3/12 16:39
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from bs4 import BeautifulSoup

with open(r'C:\Users\杨子洋\PycharmProjects\JS逆向\03 正则\250.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

tables = soup.select('table')
for table in tables:
    pl2 = table.find(class_="pl2")
    url = pl2.a['href']
    title = pl2.a.text
    comment = pl2.div.find(class_="pl").text
    print(url, title,comment)
