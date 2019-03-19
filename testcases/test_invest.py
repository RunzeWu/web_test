#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/17 17:01
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :test_invest.py
# Software  :PyCharm Community Edition
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from datas import invest
from common.mylog import get_logger
from libext.ddt import ddt, data
from common.config import ReadConfig

logger = get_logger("test_invest")
incorrect_invest_button = invest.incorrect_invest_button
incorrect_invest_toast = invest.incorrect_invest_toast


@ddt
class TestInvest(unittest.TestCase):
    # 时间问题，暂不对页面每个元素审查，只测实名认证后的用户能否正常投标

    @classmethod
    def setUpClass(cls):
        chrome_opt = webdriver.ChromeOptions()
        value = ReadConfig().get_value("chrome_options", "chrome_options")
        chrome_opt.add_argument(value)
        cls.driver = webdriver.Chrome(chrome_options=chrome_opt)
        # 先登录
        url = ReadConfig().get_value("web", "url")
        cls.driver.get(url)
        login_page = LoginPage(cls.driver)
        cls.index_page = IndexPage(cls.driver)
        login_page.submit_info("18684720553", "python")
        cls.index_page.click_loan()
        logger.info("登录成功，准备开始运行投资用例")

    def setUp(self):
        pass

    def tearDown(self):
        self.index_page.loan_input_clear()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip
    def test_correct_invest(self):
        value = invest.correct_invest
        amount = value["amount"]
        expected = value["expected"]
        logger.info("数据读取成功，充值金额：{0}，期望结果：{1}".format(amount, expected))
        self.index_page.invest(amount)

        actual = self.index_page.get_success_toast_text()
        logger.info("实际结果：{}".format(actual))
        self.index_page.click_close_pop()
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            logger.error("expected is not same as actual. error:{}".format(e))
            raise e

    @data(*incorrect_invest_button)
    def test_incorrect_invest_button(self, value):
        amount = value["amount"]
        expected = value["expected"]
        logger.info("数据读取成功，充值金额：{0}，期望结果：{1}".format(amount, expected))
        self.index_page.loan_input_sendkeys(amount)
        try:
            self.assertFalse(self.index_page.get_loan_button_ele().is_enabled())
        except AssertionError as e:
            logger.error("button应该不了点击")
            raise e
        actual = self.index_page.get_button_text()
        logger.info("实际结果：{}".format(actual))

        try:
            self.assertEqual(expected,actual)
        except AssertionError as e:
            logger.error("expected is not same as actual. error:{}".format(e))
            raise e

    # @unittest.skip
    @data(*incorrect_invest_toast)
    def test_incorrect_invest_toast(self, value):
        amount = value["amount"]
        expected = value["expected"]
        self.index_page.invest(amount)
        logger.info("数据读取成功，充值金额：{0}，期望结果：{1}".format(amount, expected))

        actual = self.index_page.get_toast_text()
        logger.info("实际结果：{}".format(actual))
        self.index_page.click_toast_button()
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            logger.error("expected is not same as actual. error:{}".format(e))
            raise e


if __name__ == '__main__':
    unittest.main()
