#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 16:52
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :login_page.py
# Software  :PyCharm Community Edition
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage(BasePage):

    user_locator = (By.XPATH,"//input[@name='phone']")
    pwd_locator = (By.XPATH,"//input[@name='password']")

    error_locator = (By.XPATH,"//div[@class='form-error-info']")
    toast_info_locator = (By.XPATH, "//div[@class='layui-layer-content']")

    def get_user_ele(self):
        return self.get_visible_element(self.user_locator)

    def get_pwd_ele(self):
        return self.get_visible_element(self.pwd_locator)

    def alert_info(self):
        return self.get_visible_element(self.error_locator).text

    def toast_info(self):
        return self.get_visible_element(self.toast_info_locator).text

    def submit_info(self,mobile,pwd):
        self.user_sendkey(mobile)
        self.pwd_sendkey(pwd)
        self.get_user_ele().submit()

    def clear_mobile(self):
        return self.get_user_ele().clear()

    def clear_pwd(self):
        return self.get_pwd_ele().clear()

    def user_sendkey(self,value):
        self.clear_mobile()
        return self.get_user_ele().send_keys(value)

    def pwd_sendkey(self, value):
        self.clear_pwd()
        return self.get_pwd_ele().send_keys(value)

    def click_mobile(self):
        return self.get_user_ele().click()

    def click_pwd(self):
        return self.get_pwd_ele().click()

if __name__ == '__main__':
    driver = webdriver.Chrome()

    loginpage = LoginPage(driver)
    url = loginpage.login_url
    driver.get(url)
    loginpage.submit_info("18684720553","python")
    # print(loginpage.get_user_ele().__annotations__)