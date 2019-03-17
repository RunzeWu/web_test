#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 17:30
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :login_page.py
# Software  :PyCharm Community Edition

user_correct = {"mobile":"18684720553","password":"python"}

user_incorrect = [
                    {"mobile":"","password":"","expected":"请输入手机号"},
                    {"mobile":"123","password":"python","expected":"请输入正确的手机号"},
                    {"mobile":"18684720553","password":"","expected":"请输入密码"}
                ]

user_toast = [{"mobile":"18684728888","password":"156", "expected":"此账号没有经过授权，请联系管理员!"},
               {"mobile": "18684720553", "password": "156", "expected": "帐号或密码错误!"}]