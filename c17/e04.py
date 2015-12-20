#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：输出为'NI'。因为全局声明会强制函数中赋值的变量引用其所在的全局作用域中的变量。
'''

# 题设代码及验证

X='Spam'
def func():
    global X
    X='NI'

func()
print(X)
