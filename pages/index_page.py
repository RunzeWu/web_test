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
    # user_locator = (By.XPATH, "// a[@href='/Member/index.html']")
    # loan_locator = (By.XPATH, "//a[text()='投标']")
    # index_locator = (By.XPATH, "//a[text()='首页']")
    # comm_locator = (By.XPATH, "//a[text()='蜂群/公社']")
    # first_loan_input_locator = (By.XPATH, "//div[@class='clearfix left']//input[1]")
    # first_loan_checkbox_locator = (By.XPATH, "//input[@type='checkbox'][1]")
    # # 投标的按钮有状态变化以及会有toast
    # first_loan_button_locator = (By.XPATH, "//button[@class='btn btn-special height_style']")
    # toast_text_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='text-center']")
    # toast_button_locator = (By.XPATH, "//a[@class='layui-layer-btn0']")
    # success_toast_text_locator = (By.XPATH, "//div[@class='capital_font1 note' and text()='投标成功！']")
    # close_success_pop_locator = (By.XPATH,
    #                              "//div[@class='capital_font1 note' and text()='投标成功！']/preceding-sibling::div//img")

    def get_user_info(self):
        return self.get_visible_element(il.user_locator).text

    @property
    def get_loan_ele(self):
        return self.get_visible_element(il.loan_locator)

    def click_loan(self):
        return self.get_loan_ele.click()

        # @property
        # def get_loan_ele(self):
        #     return self.get_visible_element(self.loan_locator)
        #
        # @property
        # def get_index_ele(self):
        #     return self.get_visible_element(self.index_locator)
        #
        # @property
        # def get_comm_ele(self):
        #     return self.get_visible_element(self.comm_locator)
        #
        # @property
        # def get_first_loan_input_ele(self):
        #     return self.get_visible_element(self.first_loan_input_locator)
        #
        # def click_loan(self):
        #     return self.get_loan_ele.click()
        #
        # def loan_input_clear(self):
        #     return self.get_first_loan_input_ele.clear()
        #
        # def loan_input_sendkeys(self, value):
        #     self.loan_input_clear()
        #     return self.get_first_loan_input_ele.send_keys(value)
        #
        # @property
        # def get_first_checkbox_ele(self):
        #     return self.get_visible_element(self.first_loan_checkbox_locator)
        #
        # @property
        # def get_loan_button_ele(self):
        #     return self.get_visible_element(self.first_loan_button_locator)
        #
        # @property
        # def get_toast_text_ele(self):
        #     return self.get_visible_element(self.toast_text_locator)
        #
        # @property
        # def get_toast_button_ele(self):
        #     return self.get_visible_element(self.toast_button_locator)
        #
        # def click_checkbox(self):
        #     return self.get_first_checkbox_ele.click()
        #
        # def click_loan_button(self):
        #     return self.get_loan_button_ele.click()
        #
        # def get_toast_text(self):
        #     return self.get_toast_text_ele.text
        #
        # def click_toast_button(self):
        #     return self.get_toast_button_ele.click()
        #
        # def get_button_text(self):
        #     return self.get_loan_button_ele.text
        #
        # @property
        # def get_success_toast_text_ele(self):
        #     return self.get_visible_element(self.success_toast_text_locator)
        #
        # def get_success_toast_text(self):
        #     return self.get_success_toast_text_ele.text
        #
        # @property
        # def get_close_success_pop_ele(self):
        #     return self.get_visible_element(self.close_success_pop_locator)
        #
        # def click_close_pop(self):
        #     return self.get_close_success_pop_ele.click()
        #
        # def invest(self, amount=None):
        #     self.loan_input_sendkeys(amount)
        #     self.click_loan_button()
