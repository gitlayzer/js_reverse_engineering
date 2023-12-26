import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
opt = webdriver.ChromeOptions()
# opt.add_argument('--headless')
opt.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(service=service, options=opt)

driver.get('https://www.5xclass.cn')
tag = driver.find_element(
    By.XPATH,
    '/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/a[1]'
)
print(tag.text)
print(tag.get_attribute("target"))
print(tag.get_attribute("data-toggle"))
time.sleep(10)
driver.close()