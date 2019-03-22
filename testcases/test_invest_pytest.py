# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/21 22:35
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :test_invest_pytest.py
# Software  :PyCharm Community Edition
import pytest
from datas import invest
from common.mylog import get_logger

logger = get_logger("test_invest")


@pytest.mark.usefixtures("bid_class_env")
@pytest.mark.usefixtures("bid_env")
class TestInvest:

    @pytest.mark.invest
    def test_correct_invest(self, bid_class_env):
        bid_page,driver = bid_class_env
        value = invest.correct_invest
        amount = value["amount"]
        expected = value["expected"]
        logger.info("数据读取成功，充值金额：{0}，期望结果：{1}".format(amount, expected))
        before_money = float(bid_page.get_invest_money())
        bid_page.invest(amount)

        actual = bid_page.get_success_toast_text()
        logger.info("实际结果：{}".format(actual))
        bid_page.click_close_pop()
        try:
            # assertEqual(expected, actual)
            assert expected == actual
        except AssertionError as e:
            logger.error("expected is not same as actual. error:{}".format(e))
            raise e

        driver.refresh()
        after_money = float(bid_page.get_invest_money())

        # bid_page.loan_input_clear()

        try:
            assert before_money - float(amount) == after_money
        except AssertionError as e:
            logger.error("money is not correct. error:{}".format(e))
            raise e

    @pytest.mark.invest
    @pytest.mark.parametrize("value", invest.incorrect_invest_button)
    def test_incorrect_invest_button(self, value, bid_class_env):
        bid_page, driver = bid_class_env
        amount = value["amount"]
        expected = value["expected"]
        logger.info("数据读取成功，充值金额：{0}，期望结果：{1}".format(amount, expected))
        bid_page.loan_input_sendkeys(amount)
        try:
            # self.assertFalse(bid_page.get_loan_button_ele.is_enabled())
            assert bid_page.get_loan_button_ele.is_enabled() is False
        except AssertionError as e:
            logger.error("button应该不了点击")
            raise e
        actual = bid_page.get_button_text()
        logger.info("实际结果：{}".format(actual))

        # bid_page.loan_input_clear()

        try:
            # self.assertEqual(expected, actual)
            assert expected == actual
        except AssertionError as e:
            logger.error("expected is not same as actual. error:{}".format(e))
            raise e

    @pytest.mark.invest
    @pytest.mark.parametrize("value", invest.incorrect_invest_toast)
    def test_incorrect_invest_toast(self, value, bid_class_env):
        bid_page, driver = bid_class_env
        amount = value["amount"]
        expected = value["expected"]
        bid_page.invest(amount)
        logger.info("数据读取成功，充值金额：{0}，期望结果：{1}".format(amount, expected))

        actual = bid_page.get_toast_text()
        logger.info("实际结果：{}".format(actual))
        bid_page.click_toast_button()

        # bid_page.loan_input_clear()

        try:
            # assertEqual(expected, actual)
            assert expected == actual
            logger.info('断言成功')
        except AssertionError as e:
            logger.error("expected is not same as actual. error:{}".format(e))
            raise e


if __name__ == '__main__':
    pytest.main(["-m invest",
                 "--html=1.html"])