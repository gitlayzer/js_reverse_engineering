# coding: utf-8
import random
from pyppeteer import launch
import asyncio
import cv2
from urllib import request


async def get_track():
    background = cv2.imread("background.png", 0)
    gap = cv2.imread("gap.png", 0)

    res = cv2.matchTemplate(background, gap, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[2][0]
    print(value)
    return value * 242 / 360


async def main():
    browser = await launch({
        "headless": False,  # headless指定浏览器是否以无头模式运行，默认是True。
        "args": ['--window-size=1366,768'],
    })
    # 打开新的标签页
    page = await browser.newPage()
    # 设置页面大小一致
    await page.setViewport({"width": 1366, "height": 768})
    # 访问主页
    await page.goto("https://passport.jd.com/new/login.aspx?")

    # evaluate()是执行js的方法，js逆向时如果需要在浏览器环境下执行js代码的话可以利用这个方法
    # js为设置webdriver的值，防止网站检测
    # await page.evaluate('''alert("马上输入用户名密码了！")''')
    # await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    # await page.screenshot({'path': './1.jpg'})   # 截图保存路径
    # 单击事件
    await page.click('div.login-tab-r')
    # 模拟输入用户名和密码,输入每个字符的间隔时间delay ms
    await page.type("#loginname", 'admin', {
        "c": random.randint(30, 60)
    })
    await page.type("#nloginpwd", 'admin1234', {
        "delay": random.randint(30, 60)
    })

    # page.waitFor 通用等待方式，如果是数字，则表示等待具体时间（毫秒）: 等待2秒
    await page.waitFor(2000)
    await page.click("div.login-btn")
    await page.waitFor(2000)
    # page.jeval（selector，pageFunction）#定位元素，并调用js函数去执行
    img_src = await page.Jeval(".JDJRV-bigimg > img", "el=>el.src")
    temp_src = await page.Jeval(".JDJRV-smallimg > img", "el=>el.src")

    request.urlretrieve(img_src, "background.png")
    request.urlretrieve(temp_src, "gap.png")

    # 获取gap的距离
    distance = await get_track()
    """
        # Pyppeteer 三种解析方式
        Page.querySelector()  # 选择器
        Page.querySelectorAll()
        Page.xpath()  # xpath  表达式
        # 简写方式为：
        Page.J(), Page.JJ(), and Page.Jx()
        """
    el = await page.J("div.JDJRV-slide-btn")
    # 获取元素的边界框，包含x,y坐标
    box = await el.boundingBox()
    await page.hover("div.JDJRV-slide-btn")
    await page.mouse.down()
    # steps 是指分成几步来完成，steps越大，滑动速度越慢
    await page.mouse.move(box["x"] + distance + random.uniform(30, 33), box["y"], {"steps": 100})
    await page.waitFor(1000)
    await page.mouse.move(box["x"] + distance + 29, box["y"], {"steps": 100})
    await page.mouse.up()
    await page.waitFor(2000)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
