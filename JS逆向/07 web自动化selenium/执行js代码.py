# coding: utf-8
"""
@python version : python3.10
@file name      : 执行js代码.py
@date           : 2024/3/15 9:55
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
# 执行滚动条

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.jd.com/')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(3)