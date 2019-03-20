# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 20:47
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :index_page.py
# Software  :PyCharm Community Edition
from selenium.webdriver.common.by import By
from pages.base import BasePage
from pages.locators.index_locator import IndexLocator as il


class IndexPage(BasePage):

    def get_user_info(self):
        return self.get_visible_element(il.user_locator).text

    @property
    def get_loan_ele(self):
        return self.get_visible_element(il.loan_locator)

    def click_loan(self):
        return self.get_loan_ele.click()
