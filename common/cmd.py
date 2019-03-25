#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/25 15:03
# @Author   : Yosef-夜雨声烦
# @Email    : wurz529@foxmail.com
# @File     : cmd.py
# @Software : PyCharm
import os
from common import contants


def exc_allure_serve():
    allure_dir = contants.allure_dir
    command = "allure serve "+allure_dir
    # print(command)
    return os.system(command)


if __name__ == '__main__':
    exc_allure_serve()