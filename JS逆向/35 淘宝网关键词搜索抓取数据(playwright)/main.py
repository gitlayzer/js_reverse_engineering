# coding: utf-8
"""
@python version : python3.10
@file name      : main.py
@date           : 2024/4/25 13:29
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from lxml import etree
from playwright.sync_api import sync_playwright


def get_content(page):
    # 一边滚动一边加载页面
    for i in range(10):
        page.mouse.wheel(0, 600)
        page.wait_for_timeout(1100)
    # 获取源码数据页面
    page_text = page.content()
    html = etree.HTML(page_text)
    div_list = html.xpath('//*[@id="pageContent"]/div[1]/div[3]/div[3]/div/div')
    for div in div_list:
        title = div.xpath('./a/div/div[1]/div[2]/div/span/text()')
        print(title)


def playwright_run():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp('http://localhost:8899/')
        page = browser.contexts[0].pages[0]
        # 输入框输入关键词 比如 笔记本电脑
        page.locator('//*[@id="q"]').fill('笔记本电脑')
        # 点击搜索,获取第一页页面信息
        page.locator('//*[@id="button"]').click()
        get_content(page)
        for _ in range(10): # 10为点击十次
            # 获取下一页标签
            page.locator('//*[@id="pageContent"]/div[1]/div[3]/div[4]/div/div/button[2]').click()
            # 获取下一页页面信息
            get_content(page)


if __name__ == '__main__':
    playwright_run()