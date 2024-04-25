# coding: utf-8
"""
@python version : python3.10
@file name      : 规避检测.py
@date           : 2024/4/25 11:01
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     bro = p.chromium.launch(headless=False)
#     page = bro.new_page()
#     page.goto('https://www.taobao.com/')
#
#     ret = page.evaluate('window.navigator.webdriver')
#     print(ret)
#
#     page.wait_for_timeout(30000)
#     page.close()
#     bro.close()


# js注入

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    bro = p.chromium.launch(headless=False)
    context = bro.new_context()
    #加载该js文件目的是给Playwright的浏览器模拟真实的浏览器环境
    context.add_init_script(path='./stealth.min.js')
    page = context.new_page()
    page.goto('https://www.taobao.com/')

    ret = page.evaluate('window.navigator.webdriver')
    print(ret)

    page.wait_for_timeout(30000)
    page.close()
    bro.close()