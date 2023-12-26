import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://passport.bilibili.com/login')

time.sleep(10)
driver.close()
