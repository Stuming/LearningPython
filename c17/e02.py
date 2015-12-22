#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：输出为'Spam'。在函数中赋值变量会将其变成本地变量，从而隐藏同名的全局变量。但print语句会找到没有发生改变的全局(模块)作用域中的变量。
'''

# 题设代码及验证

X='Spam'
def func():
    X='NI'

func()
print(X)
