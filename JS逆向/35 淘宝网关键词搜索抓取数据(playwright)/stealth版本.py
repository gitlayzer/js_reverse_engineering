import re
from playwright.sync_api import Playwright, sync_playwright, expect
from lxml import etree


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")
    context.add_init_script(path='./stealth.min.js')
    page = context.new_page()
    page.goto("https://www.taobao.com/")
    page.get_by_label("请输入搜索文字").click()
    page.get_by_label("请输入搜索文字").fill("笔记本电脑")
    page.get_by_role("button", name="搜索").click()
    for i in range(15):
        page.mouse.wheel(0, 600)
        page.wait_for_timeout(1100)
    # 获取源码数据页面
    page_text = page.content()
    html = etree.HTML(page_text)
    div_list = html.xpath('//*[@id="pageContent"]/div[1]/div[3]/div[3]/div/div')
    for div in div_list:
        title = div.xpath('./a/div/div[1]/div[2]/div/span/text()')
        print(title)
    # page.locator("button").filter(has_text="下一页").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
