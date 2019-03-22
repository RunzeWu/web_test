# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/21 22:39
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :conftest.py
# Software  :PyCharm Community Edition
import pytest
from selenium import webdriver
from pages import login_page
from common.config import ReadConfig
from pages.bid_page import BidPage
from pages.index_page import IndexPage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def login_class_env():
    chrome_opt = webdriver.ChromeOptions()
    value = ReadConfig().get_value("chrome_options", "chrome_options")
    chrome_opt.add_argument(value)
    # driver = webdriver.Chrome(chrome_options=chrome_opt)
    driver = webdriver.Chrome()
    login = login_page.LoginPage(driver)
    url = ReadConfig().get_value("web", "url")
    driver.get(url)

    yield driver, login

    driver.quit()


@pytest.fixture(scope="class")
def bid_class_env():

    chrome_opt = webdriver.ChromeOptions()
    value = ReadConfig().get_value("chrome_options", "chrome_options")
    chrome_opt.add_argument(value)
    # chrome_options = chrome_opt
    driver = webdriver.Chrome()
    # 先登录
    url = ReadConfig().get_value("web", "url")
    driver.get(url)
    login_page = LoginPage(driver)
    bid_page = BidPage(driver)
    index_page = IndexPage(driver)
    login_page.submit_info("18684720553", "python")
    index_page.click_loan()

    yield bid_page,driver

    driver.quit()