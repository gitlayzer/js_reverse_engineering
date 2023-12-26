import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://www.autohome.com.cn/beijing/')

# ############### 1.单独找到每一个 ###############
tag = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]/label[1]/span/input'
)
print(tag.get_property("checked")) # True


tag = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]/label[2]/span/input'
)
print(tag.get_property("checked")) # False

# ############### 2.循环找到每一个 ###############
parent = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[11]/div[2]/div[1]/div[1]'
)

tag_list = parent.find_elements(
    By.XPATH,
    'label/span/input'
)
for tag in tag_list:
    print( tag.get_property("checked"), tag.get_attribute("value") )

driver.close()