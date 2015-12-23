#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：输出为1 (2,3)。因为1按位置赋值给了a，额外未分配的2和3被*pargs收集到一个元组中。
'''

# 题设代码及验证
def func(a, *pargs):
    print(a, pargs)

func(1, 2, 3)
