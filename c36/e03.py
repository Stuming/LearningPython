#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：Python 2.6和Python 3.0中的字符串类型是如何对应的？
答：它们之间的对应不是直接的：
    针对文本类型，Python 3.0中的str类型相当于2.6中的str加上unicode类型；
    针对二进制数据，2.6中的str类型和3.0中的bytes类型对应；
    bytearray类型是3.0中独有的。
'''
