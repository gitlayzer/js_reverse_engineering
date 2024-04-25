# coding: utf-8
"""
@python version : python3.10
@file name      : 获取淘宝某商品评论.py
@date           : 2024/4/25 16:01
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
from playwright.sync_api import Playwright, sync_playwright, expect
from lxml import etree


# 封装页面切换的函数
def switch_to_page(context, title):
    for page in context.pages:
        if title == page.title():
            # 浏览器停留在此page页面
            page.bring_to_front()
            return page


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="./auth.json")
    context.add_init_script(path='./stealth.min.js')
    page = context.new_page()
    page.goto("https://www.taobao.com/")
    page.get_by_label("请输入搜索文字").click()
    page.get_by_label("请输入搜索文字").fill("手机")
    page.get_by_role("button", name="搜索").click()
    page.wait_for_timeout(5000)
    # 获取一个商品的详情页
    # 点击商品的详情页
    page.locator('//*[@id="pageContent"]/div[1]/div[3]/div[3]/div/div[2]/a').click()
    page.wait_for_timeout(5000)
    # 根据详情页标题 获取详情页数据
    detail_page = context.pages[1]
    detail_page.bring_to_front()
    # 点击详情页宝贝评论
    detail_page.locator('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/span').click()
    page.wait_for_timeout(3000)
    # 滑动窗口展开当前页所有评论
    for i in range(15):
        detail_page.mouse.wheel(0, 600)
        detail_page.wait_for_timeout(1100)
    # 获取源码数据页面
    page_text = detail_page.content()
    html = etree.HTML(page_text)
    div_list = html.xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div')
    for div in div_list:
        comment = div.xpath('./div[1]/div[2]/text()')[0]
        re_comment = div.xpath('./div[1]/div[3]/div/span[2]/text()')
        print(comment, re_comment)
    page.close()

    # ---------------------
    context.close()
    browser.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
