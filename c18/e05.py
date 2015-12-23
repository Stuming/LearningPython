#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：输出为1 5 6 4。1按位置赋值给a，(5, 6)经*name语法解包后也按位置顺序传递给b和c，d则使用的是默认值4。
'''

# 题设代码及验证
def func(a, b, c=3, d=4): print(a, b, c, d)

func(1, *(5, 6))
