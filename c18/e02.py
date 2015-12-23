#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：输出为1 2 3。因为函数调用时参数1按位置赋值给a，而b与c是通过关键字参数赋值的。
'''

# 题设代码及验证
def func(a, b, c=5):
    print(a, b, c)

func(1, c=3, b=2)
