import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 注意：一定要先访问，不然Cookie无法生效
driver.get('https://dig.chouti.com/about')

# 加cookie
driver.add_cookie({
    'name': 'token',
    'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqaWQiOiJjZHVfNDU3OTI2NDUxNTUiLCJleHBpcmUiOiIxNzA0MzI5NDY5OTMyIn0.8n_tWcEHXsBSXWIY9rBoGWwaLPF8iWIruryhKTe5_ks'
})

# 再访问
driver.get('https://dig.chouti.com/')

time.sleep(2000)
driver.close()