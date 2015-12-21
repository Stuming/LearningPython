#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：输出为'Spam'。因为函数引用的是所在模块中的全局变量
'''

# 题设代码及验证

X='Spam'
def func():
    print(X)

func()
