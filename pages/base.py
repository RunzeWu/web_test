#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 16:53
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :base.py
# Software  :PyCharm Community Edition
import time
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common import mylog
from selenium import webdriver

logger = mylog.get_logger("basepage")

class BasePage:

    def __init__(self,driver:Chrome):
        self.driver = driver

    def get_visible_element(self, locator, eqc=20) -> WebElement:
        try:
            return WebDriverWait(self.driver, eqc).until(
                    EC.visibility_of_element_located(locator))
        except Exception as e:
            logger.error("相对时间内没有定位到该元素,异常信息是{}".format(e))
            # self.driver.save_screenshot("/logs{}.png".format(time.time))

if __name__ == '__main__':
    user_locator = (By.XPATH, "//input[@name='phone']")
    pwd_locator = (By.XPATH, "//input[@name='password']")
    driver = webdriver.Chrome()
    A = BasePage(driver)
    driver.get('http://120.79.176.157:8012/Index/login.html')
    A.get_visible_element(user_locator).send_keys("11111")


