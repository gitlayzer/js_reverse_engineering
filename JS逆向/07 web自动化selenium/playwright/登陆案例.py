# coding: utf-8
"""
@python version : python3.10
@file name      : 登陆案例.py
@date           : 2024/4/28 9:52
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://download.java1234.com/")
    page.get_by_text('登录').click()
    page.wait_for_timeout(3000)
    # 点击登录按钮获取登录框
    frame = page.frame(name='layui-layer-iframe1')
    frame.locator('#userName').fill('xxxxxxxx')
    frame.locator('#password').fill('xxxxx%')
    frame.get_by_text('登录').click()
    frame.wait_for_timeout(10000)
    # ---------------------
    context.close()
    browser.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
