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


@pytest.fixture(scope="class", autouse=True)
def login_class_env():
    chrome_opt = webdriver.ChromeOptions()
    value = ReadConfig().get_value("chrome_options", "chrome_options")
    chrome_opt.add_argument(value)
    # driver = webdriver.Chrome(chrome_options=chrome_opt)
    driver = webdriver.Chrome()
    login = login_page.LoginPage(driver)

    yield driver, login

    driver.quit()


@pytest.mark.usefixtrues("")
@pytest.fixture
def login_case_env(driver):
    url = ReadConfig().get_value("web", "url")
    driver.get(url)
    yield driver
