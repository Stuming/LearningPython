#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：输出为1 {'c':3, 'b':2}。1通过名称传递给a，额外未匹配的关键字参数被**kargs收集到一个字典中。
'''

# 题设代码及验证
def func(a, **kargs):
    print(a, kargs)

func(a=1, c=3, b=2)
