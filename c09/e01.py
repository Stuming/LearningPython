#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
你怎么确定元组有多大？

答：可以使用Python内置的len函数，会传回Python中包括元组在内的任何容器对象的长度（所含元素的数目），适用于多种对象。
"""

#Example:
T = (1,'a','b','c','d','e')
num = len(T)
print("T的长度为:",num)
