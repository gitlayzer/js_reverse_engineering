# coding: utf-8
"""
@python version : python3.10
@file name      : 滑动验证登录.py
@date           : 2024/3/15 10:15
@author         : ziyang.yang@aliyun.com
@gitee          : https://gitee.com/ziyangyang1318
@blog           : www.yangziyang.top
@describe       : 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from urllib.request import urlretrieve
import cv2
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素


# 通过open cv 获取缺口在背景图片中的位置
def get_distance():
    background = cv2.imread("background.png", 0)
    gap = cv2.imread("gap.png", 0)

    res = cv2.matchTemplate(background, gap, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[2][0]
    print(value)
    return value * 242 / 360


def main():
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(5)  # 隐式等待

    # 请求页面
    chrome.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
    # 获取用户名输入框
    login_name = chrome.find_element(By.XPATH, '//*[@id="loginname"]')
    # 输入框输入用户名
    login_name.send_keys('admin')
    # 获取密码输入框
    login_pwd = chrome.find_element(By.XPATH, '//*[@id="nloginpwd"]')
    # 输入密码
    login_pwd.send_keys('Admin123')
    # 获取登录按钮
    submit = chrome.find_element(By.XPATH, '//*[@id="loginsubmit"]')
    submit.click()
    time.sleep(5)
    # 获取背景图片,并下载到本地
    background_img = chrome.find_element(By.XPATH,
                                         '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img').get_attribute(
        'src')
    # 获取缺口图片，并下载到本地
    gap_img = chrome.find_element(By.XPATH,
                                  '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img').get_attribute(
        'src')
    # 将图片下载到本地
    urlretrieve(background_img, 'background.png')
    urlretrieve(gap_img, 'gap.png')

    # 计算滑动距离
    distance = get_distance()

    # 动作链滑动
    print('第一步,点击滑动按钮')
    element = chrome.find_element(By.CLASS_NAME, 'JDJRV-slide-btn')
    ActionChains(chrome).click_and_hold(on_element=element).perform()  # 点击鼠标左键，按住不放
    # 向x轴 右平移
    ActionChains(chrome).move_by_offset(xoffset=int(distance), yoffset=0).perform()
    ActionChains(chrome).release(on_element=element).perform()
    time.sleep(5)


# chrome.close()

if __name__ == '__main__':
    main()
    """
    滑动太快，会被识别为机器
    """