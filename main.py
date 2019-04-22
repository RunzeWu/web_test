# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/23 10:49
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :main.py
# Software  :PyCharm Community Edition
import pytest
from common.cmd import exc_allure_serve


if __name__ == '__main__':
    pytest.main(["-m pytest",
                 "--alluredir=allure"])

# 可以选择脚本运行结束之后执行cmd命令，也可以忽略
exc_allure_serve()
