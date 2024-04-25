# coding: utf-8
"""
@python version : python3.10
@file name      : 异步版本.py
@date           : 2024/4/25 14:41
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""

import asyncio
from lxml import etree
from playwright.async_api import async_playwright, Playwright


async def get_content(page):
    # 一边滚动一边加载页面
    for i in range(10):
        await page.mouse.wheel(0, 600)
        await page.wait_for_timeout(1100)
    # 获取源码数据页面
    page_text = await page.content()
    html = etree.HTML(page_text)
    div_list = html.xpath('//*[@id="pageContent"]/div[1]/div[3]/div[3]/div/div')
    for div in div_list:
        title = div.xpath('./a/div/div[1]/div[2]/div/span/text()')
        print(title)


async def run(playwright: Playwright):
    browser = await playwright.chromium.connect_over_cdp('http://localhost:8899/')
    page = browser.contexts[0].pages[0]
    # 输入框输入关键词 比如 笔记本电脑
    await page.locator('//*[@id="q"]').fill('笔记本电脑')
    # 点击搜索,获取第一页页面信息
    await page.locator('//*[@id="button"]').click()
    await get_content(page)
    for _ in range(10):  # 10为点击十次
        # 获取下一页标签
        await page.locator('//*[@id="pageContent"]/div[1]/div[3]/div[4]/div/div/button[2]').click()
        # 获取下一页页面信息
        await get_content(page)


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())
