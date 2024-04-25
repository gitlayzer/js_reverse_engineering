# coding: utf-8
"""
@python version : python3.10
@file name      : JS注入.py
@date           : 2024/4/25 11:45
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
      browser = p.chromium.launch(headless=True)
      context = browser.new_context()
      #规避检测，伪造真实浏览器环境
      context.add_init_script(path='stealth.min.js')
      page = context.new_page()
      page.goto("https://www.ciweimao.com/chapter/109936632")
      page.wait_for_timeout(3000)
    # #进行js注入，执行解密js代码
      encrypt_data = page.evaluate('$.myDecrypt({content: messageInfo,keys: keys,accessKey: HB.config.chapterAccessKey})')
      print(encrypt_data)