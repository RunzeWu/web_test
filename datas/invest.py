#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/18 10:07
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : invest.py
# @Software : PyCharm

correct_invest = {"amount": "1000", "expected": "投标成功！", "title": "正常投标"}

incorrect_invest_button = [{"amount": "1001", "expected": "请输入10的整数倍", "title": "投不能被10整除的正数"},
                           {"amount": "a80", "expected": "请输入10的整数倍", "title": "投字符"}
                           ]

incorrect_invest_toast = [
    {"amount": "-10", "expected": "请正确填写投标金额", "title": "投负数"},
    {"amount": "1000000000000000", "expected": "投标金额大于可用金额", "title": "投大于可用金额的数"}
]
