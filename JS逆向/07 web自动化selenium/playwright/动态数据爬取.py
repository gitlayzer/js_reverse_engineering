# coding: utf-8
"""
@python version : python3.10
@file name      : 动态数据爬取.py
@date           : 2024/4/25 9:36
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

from playwright.sync_api import sync_playwright
from lxml import etree

with sync_playwright() as p:
    # 创建浏览器
    bro = p.chromium.launch(headless=False)
    # 创建页面
    page = bro.new_page()
    page.goto("https://jzsc.mohurd.gov.cn/data/company")
    # 等待2秒 加载页面数据
    page.wait_for_timeout(2000)
    # 获取页面源码数据
    page_html = page.content()  # 这是刚进来是第一页的数据
    page_html_list = [page_html, ]
    # 点下一页按钮，将所有的页面数据添加到列表中
    for page_num in range(1, 10):
        # 获取下一页按钮并点击
        page.locator('//*[@id="app"]/div/div/div[2]/div[3]/div[2]/button[2]').click()
        page.wait_for_timeout(2000)
        next_html = page.content()
        # 获取点击之后页面的源码数据，并添加到列表中
        page_html_list.append(next_html)
    # 针对源码数据列表遍历，进行数据解析
    for page_text in page_html_list:
        print(f'正在获取当前页数据...')
        tree = etree.HTML(page_text)
        tr_list = tree.xpath('//*[@id="app"]/div/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr')
        for tr in tr_list:
            # 获取社会统一信用代码
            code_num = tr.xpath('./td[2]/div/text()')[0].strip()
            # 获取企业名称
            company = tr.xpath('./td[3]/div/span/text()')[0].strip()
            # 获取法定代表人
            boss = tr.xpath('./td[4]/div/text()')[0].strip()
            # 获取企业注册地址
            addr = tr.xpath('./td[5]/div/text()')[0].strip()
            print(code_num, company, boss, addr)

    page.close()
    bro.close()
