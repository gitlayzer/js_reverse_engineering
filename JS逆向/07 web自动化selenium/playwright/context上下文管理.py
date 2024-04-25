# coding: utf-8
"""
@python version : python3.10
@file name      : context上下文管理.py
@date           : 2024/4/25 10:09
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 对于打开的页面会新增一个页面，获取新增，或者切换多个页面的数据
"""

from playwright.sync_api import sync_playwright


# 点击百度首页中左上角的全部链接，以打开多个不同的page页面
with sync_playwright() as p:
    bro = p.chromium.launch(headless=False, slow_mo=1000)
    # 创建上下文管理对象
    context = bro.new_context()
    # 基于上下文管理对象创建page对象
    page = context.new_page()
    page.goto("https://www.baidu.com")
    # 获取 几个标题的a标签，并循环点击
    a_list = page.locator('//*[@id="s-top-left"]/a').all()
    for a in a_list:
        a.click()

    # 可以获取上下文管理对象目前创建好的所有的page页面
    pages = context.pages # 获取打开的a标签对应的页面，打印他们的标题
    for page in pages:
        title = page.title()
        print(title)
    page.close()
    bro.close()