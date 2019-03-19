# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/19 22:21
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :bid_locator.py
# Software  :PyCharm Community Edition
from selenium.webdriver.common.by import By


class BidLocator:
    loan_locator = (By.XPATH, "//a[text()='投标']")
    index_locator = (By.XPATH, "//a[text()='首页']")
    comm_locator = (By.XPATH, "//a[text()='蜂群/公社']")
    first_loan_input_locator = (By.XPATH, "//div[@class='clearfix left']//input[1]")
    first_loan_checkbox_locator = (By.XPATH, "//input[@type='checkbox'][1]")
    # 投标的按钮有状态变化以及会有toast
    first_loan_button_locator = (By.XPATH, "//button[@class='btn btn-special height_style']")
    toast_text_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='text-center']")
    toast_button_locator = (By.XPATH, "//a[@class='layui-layer-btn0']")
    success_toast_text_locator = (By.XPATH, "//div[@class='capital_font1 note' and text()='投标成功！']")
    close_success_pop_locator = (By.XPATH,
                                 "//div[@class='capital_font1 note' and text()='投标成功！']/preceding-sibling::div//img")
