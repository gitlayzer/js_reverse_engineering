import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    page.goto("https://www.jd.com/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="手机", exact=True).click()

    page1 = page1_info.value
    res = page1.locator('//*[@id="J_goodsList"]/ul/li')
    count = res.count()
    # li_1 = res.nth(2)
    # print(li_1.inner_text())
    for index in range(count):
        ele = res.nth(index)
        price = ele.locator('.p-price strong i').inner_text()
        shop_name = ele.locator('.p-shop span a').inner_text()
        detail = ele.locator('.p-name-type-2 a em').inner_text()
        print(detail,price,shop_name)

    page1.close()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
