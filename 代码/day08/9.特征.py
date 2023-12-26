import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")

opt = webdriver.ChromeOptions()

opt.add_argument('--disable-infobars')
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=service, options=opt)

# Selenium在打开任何页面之前，先运行这个Js文件。
with open('driver/hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})

driver.get('https://www.5xclass.cn')

time.sleep(2000)
driver.close()