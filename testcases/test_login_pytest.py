# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/21 22:36
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :test_login_pytest.py
# Software  :PyCharm Community Edition
import pytest
from datas import login
from common.mylog import get_logger
from pages import index_page

logger = get_logger("test_login")


@pytest.mark.usefixtures("login_class_env")
class TestLogin:
    driver, login_page = login_class_env

    @pytest.mark.usefixtures("login_class_env")
    @pytest.mark.usefixtures("login_case_env")
    @pytest.mark.parametrize("value", login.user_incorrect)
    @pytest.mark.pytest
    def test_login_incorrect_form(self, value, login_class_env, login_case_env):
        driver, login_page = login_class_env
        login_case_env(driver)
        phone = value["mobile"]
        pwd = value["password"]
        expected = value["expected"]

        login_page.submit_info(phone, pwd)

        try:
            # self.assertEqual(expected, self.login.alert_info())
            assert expected == login_page.alert_info
        except AssertionError as e:
            logger.error("实际结果与预期结果不匹配，message：{}".format(e))
            raise e

    @pytest.mark.pytest
    @pytest.mark.usefixtures("login_class_env")
    @pytest.mark.parametrize("value", login.user_toast)
    def test_login_incorrect_toast(self, value, login_class_env, login_case_env):
        driver, login_page = login_class_env
        login_case_env(driver)
        phone = value["mobile"]
        pwd = value["password"]
        expected = value["expected"]

        login_page.submit_info(phone, pwd)

        try:
            # self.assertEqual(expected, self.login.toast_info())
            assert expected == login_page.toast_info
        except AssertionError as e:
            logger.error("实际结果与预期结果不匹配，message：{}".format(e))
            raise e

    @pytest.mark.pytest
    @pytest.mark.usefixtures("login_class_env")
    def test_login_correct(self, login_class_env, login_case_env):
        driver, login_page = login_class_env
        driver = login_case_env(driver)
        phone = login.user_correct["mobile"]
        pwd = login.user_correct["password"]
        expected = login.user_correct["expected"]

        login_page.submit_info(phone, pwd)
        actual = index_page.IndexPage(driver).get_user_info()
        driver.delete_all_cookies()
        try:
            # self.assertIn(expected, actual)
            assert expected in actual
        except AssertionError as e:
            logger.error("用户名不匹配,message:{}".format(e))
            raise e


if __name__ == '__main__':
    pytest.main(["-m pytest"])
