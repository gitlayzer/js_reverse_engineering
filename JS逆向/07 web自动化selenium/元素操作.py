# coding: utf-8
"""
@python version : python3.10
@file name      : 元素操作.py
@date           : 2024/3/15 9:22
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time
chrome = webdriver.Chrome()

#
# chrome.get('https://www.psi-gene.com/')
# li_list = chrome.find_elements(By.XPATH, '//*[@id="app"]/div/header/div/div[3]/ul/li')
# for li in li_list:
#     print(li.text)
# chrome.close()
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

q = browser.find_element(By.ID, "q")
q.send_keys('MAC')
time.sleep(1)
q.clear()
q.send_keys('IPhone')
button = browser.find_element(By.CLASS_NAME, "btn-search")
button.click()