#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/18 14:38
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : run.py
# @Software : PyCharm
import unittest
from libext import HTMLTestRunnerNew
from common import contants

discover = unittest.defaultTestLoader.discover(contants.testcases_dir, pattern="test_*.py", top_level_dir=None)

with open(contants.reports_html, "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="前程贷web登录，投资测试报告",
                                              description="测试了登录，投资",
                                              tester="夜雨声烦")
    runner.run(discover)
