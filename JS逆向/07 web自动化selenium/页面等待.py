# coding: utf-8
"""
@python version : python3.10
@file name      : 页面等待.py
@date           : 2024/3/15 9:59
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome()
chrome.get('')
 # 每隔 0.5s 检查一次(默认就是 0.5s), 最多等待 10 秒,否则报错。如果定位到元素则直接结束等待，如果在10秒结束之后仍未定位到元素则报错
wait = WebDriverWait(chrome, 10,0.5)
wait.until(EC.presence_of_element_located((By.ID, 'J_goodsList')))