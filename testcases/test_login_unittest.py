# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 18:18
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :test_login_unittest.py
# Software  :PyCharm Community Edition
import unittest
from common.config import ReadConfig
from libext.ddt import ddt, data
from pages import login_page
from selenium import webdriver
from datas import login
from pages import index_page
from common.mylog import get_logger

logger = get_logger("test_login")


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_opt = webdriver.ChromeOptions()
        value = ReadConfig().get_value("chrome_options", "chrome_options")
        chrome_opt.add_argument(value)
        cls.driver = webdriver.Chrome(chrome_options=chrome_opt)
        cls.login = login_page.LoginPage(cls.driver)

    def setUp(self):
        # login_url = "http://120.79.176.157:8012/Index/login.html"
        # self.driver.get(login_url)
        url = ReadConfig().get_value("web", "url")
        self.driver.get(url)

    def tearDown(self):
        # self.login.clear_mobile()
        # self.login.clear_pwd()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*login.user_incorrect)
    def test_login_incorrect_form(self, value):
        phone = value["mobile"]
        pwd = value["password"]
        expected = value["expected"]

        self.login.submit_info(phone, pwd)

        try:
            self.assertEqual(expected, self.login.alert_info)
        except AssertionError as e:
            logger.error("实际结果与预期结果不匹配，message：{}".format(e))
            raise e

    @data(*login.user_toast)
    def test_login_incorrect_toast(self, value):
        phone = value["mobile"]
        pwd = value["password"]
        expected = value["expected"]

        self.login.submit_info(phone, pwd)

        try:
            self.assertEqual(expected, self.login.toast_info)
        except AssertionError as e:
            logger.error("实际结果与预期结果不匹配，message：{}".format(e))
            raise e

    def test_login_correct(self):
        phone = login.user_correct["mobile"]
        pwd = login.user_correct["password"]
        expected = login.user_correct["expected"]

        self.login.submit_info(phone, pwd)
        actual = index_page.IndexPage(self.driver).get_user_info()
        self.driver.delete_all_cookies()
        try:
            self.assertIn(expected, actual)
        except AssertionError as e:
            logger.error("用户名不匹配,message:{}".format(e))
            raise e

