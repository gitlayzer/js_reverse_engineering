# coding: utf-8
"""
@python version : python3.10
@file name      : B站关键此搜索页面抓取.py
@date           : 2024/4/25 10:29
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from playwright.sync_api import sync_playwright
from lxml import etree

# 封装页面切换的函数
def switch_to_page(context, title):
    for page in context.pages:
        if title == page.title():
            # 浏览器停留在此page页面
            page.bring_to_front()
            return page


# 点击百度首页中左上角的全部链接，以打开多个不同的page页面
with sync_playwright() as p:
    bro = p.chromium.launch(headless=False, slow_mo=1000)
    # 创建上下文管理对象
    context = bro.new_context()
    # 基于上下文管理对象打开一个page页面
    page = context.new_page()
    page.goto('https://www.bilibili.com/')

    #  关键词搜索点击跳转
    page.locator('//*[@id="nav-searchform"]/div[1]/input').fill('JS逆向')
    page.locator('//*[@id="nav-searchform"]/div[2]').click()

    # 切换到新打开的页面
    select_page = switch_to_page(context,'JS逆向-哔哩哔哩_Bilibili')
    # 获取对应的div标签
    page_text = select_page.content()
    tree = etree.HTML(page_text)

    div_list = tree.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[2]/div/div')
    for div in div_list:
        title = div.xpath('./div/div[2]/div/div/a/h3/@title')[0].strip()
        author = div.xpath('./div/div[2]/div/div/p/a/span[1]/text()')[0].strip()
        print(title,author)

    page.close()
    bro.close()