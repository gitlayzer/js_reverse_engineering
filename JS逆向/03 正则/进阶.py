# coding: utf-8
"""
@python version : python3.10
@file name      : 进阶.py
@date           : 2024/3/12 14:26
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import re

text = '<12> <xyz> <!@#$%> <1a!#e2> <>'
# 匹配<>所有内容,利用？取消贪婪匹配

res = re.findall("<.+?>", text)
# print(res)  # ['<12>', '<xyz>', '<!@#$%>', '<1a!#e2>']

# 获取豆瓣电新片排行榜 详情页、标题、评分
with open('250.html', 'r', encoding='utf-8') as f:
    data = f.read()

ret = re.findall('<a class="nbg" href="(https://movie.douban.com/subject/\d+/)".*?title="(.+?)">.*?<div class="star clearfix">.*?<span class="rating_nums">(.+?)</span>.*?<span class="pl">\((.+?)\)</span>',data,re.S)
print(ret)


