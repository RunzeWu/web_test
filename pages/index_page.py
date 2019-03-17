#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 20:47
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :index_page.py
# Software  :PyCharm Community Edition
from selenium.webdriver.common.by import By

from pages.base import BasePage


class IndexPage(BasePage):
    user_locator = (By.XPATH,"// a[@href='/Member/index.html']")
    loan_locator = (By.XPATH,"//span[@class='active']")
    index_locator = (By.XPATH,"//a[text()='首页']")
    comm_locator = (By.XPATH,"//a[text()='蜂群/公社']")
    first_loan_input_locator = (By.XPATH,"//div[@class='clearfix left']//input[1]")
    first_loan_checkbox_locator = (By.XPATH, "//input[@type='checkbox'][1]")
    # 投标的按钮有状态变化以及会有toast
    first_loan_button_locator = (By.XPATH, "//button[@class='btn btn-special height_style']")
    toast_text_locator = (By.XPATH,"//div[@class='text-center']")
    toast_button_locator = (By.XPATH, "//a[@class='layui-layer-btn0']")


    def get_user_info(self):
        return self.get_visible_element(self.user_locator).text

    def get_loan_ele(self):
        return self.get_visible_element(self.loan_locator)

    def get_index_ele(self):
        return self.get_visible_element(self.index_locator)

    def get_comm_ele(self):
        return self.get_visible_element(self.comm_locator)

    def get_first_loan_input_ele(self):
        return self.get_visible_element(self.first_loan_input_locator)

    def click_loan(self):
        return self.get_loan_ele().click()

    def loan_input_clear(self):
        return self.get_first_loan_input_ele().clear()

    def loan_input_sendkeys(self):
        return self.get_first_loan_input_ele().click()

    def get_first_checkbox_ele(self):
        return self.get_visible_element(self.first_loan_checkbox_locator)

    def get_loan_button_ele(self):
        return self.get_visible_element(self.first_loan_button_locator)

    def get_toast_text_ele(self):
        return self.get_visible_element(self.toast_text_locator)

    def get_toast_button_ele(self):
        return self.get_visible_element(self.toast_button_locator)

    def click_checkbox(self):
        return self.get_first_checkbox_ele().click()

    def click_loan_button(self):
        return self.get_loan_button_ele().click()

    def get_toast_text(self):
        return self.get_toast_text_ele().text

    def click_toast_button(self):
        return self.get_toast_button_ele().click()