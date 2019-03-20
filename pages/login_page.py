# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 16:52
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :login_page.py
# Software  :PyCharm Community Edition

from pages.base import BasePage
from pages.locators.login_locator import LoginLocators as ll


class LoginPage(BasePage):

    def get_user_ele(self):
        return self.get_visible_element(ll.user_locator)

    def get_pwd_ele(self):
        return self.get_visible_element(ll.pwd_locator)

    def alert_info(self):
        return self.get_visible_element(ll.error_locator).text

    def toast_info(self):
        return self.get_visible_element(ll.toast_info_locator).text

    def submit_info(self, mobile, pwd):
        self.user_sendkey(mobile)
        self.pwd_sendkey(pwd)
        self.get_user_ele().submit()

    def clear_mobile(self):
        return self.get_user_ele().clear()

    def clear_pwd(self):
        return self.get_pwd_ele().clear()

    def user_sendkey(self, value):
        self.clear_mobile()
        return self.get_user_ele().send_keys(value)

    def pwd_sendkey(self, value):
        self.clear_pwd()
        return self.get_pwd_ele().send_keys(value)

    def click_mobile(self):
        return self.get_user_ele().click()

    def click_pwd(self):
        return self.get_pwd_ele().click()
