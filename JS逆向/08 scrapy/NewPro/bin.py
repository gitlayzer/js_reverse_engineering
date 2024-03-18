# coding: utf-8
"""
@python version : python3.10
@file name      : bin.py
@date           : 2024/3/15 14:45
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'wangyi', "--nolog"])
# execute(['scrapy', 'crawl', 'wangyi'])