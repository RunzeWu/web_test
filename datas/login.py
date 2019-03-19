# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2019/3/16 17:30
# @Author   :Yosef-夜雨声烦
# E-mail    :wurz529@foxmail.com
# File      :login_page.py
# Software  :PyCharm Community Edition

user_correct = {"mobile": "18684720553", "password": "python", "expected": "小蜜蜂", "title": "正常登录"}

user_incorrect = [
    {"mobile": "", "password": "", "expected": "请输入手机号", "title": "空账号密码"},
    {"mobile": "123", "password": "python", "expected": "请输入正确的手机号", "title": "错误的手机号"},
    {"mobile": "18684720553", "password": "", "expected": "请输入密码", "title": "空密码"}
]

user_toast = [{"mobile": "18684728888", "password": "156", "expected": "此账号没有经过授权，请联系管理员!", "title": "未授权账号"},
              {"mobile": "18684720553", "password": "156", "expected": "帐号或密码错误!", "title": "账号密码错误"}]
