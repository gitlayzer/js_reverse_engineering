# coding: utf-8
"""
@python version : python3.10
@file name      : 浏览器接管.py
@date           : 2024/4/25 11:14
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from playwright.sync_api import sync_playwright
from lxml import etree

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:8899/')
    # 获取page对象
    page = browser.contexts[0].pages[0]
    #该操作会直接作用在接管的浏览器中
    page.locator('//*[@id="searchKey"]').fill('上海')
    page.get_by_text('查一下').click()
    page.wait_for_timeout(6000)
    page_text = page.content()
    tree = etree.HTML(page_text)
    tr_list = tree.xpath('/html/body/div/div[2]/div[2]/div[3]/div/div[2]/div/table/tr')
    for tr in tr_list:
        company = tr.xpath('./td[3]/div/span/span[1]/a/span//text()')
        print(company)

