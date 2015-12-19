#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
如何获得对象中可用属性的列表？

答：利用内置的dir(x)函数，可以返回附加在任何对象上的所有属性的列表。
'''

# Example

m = 1
print('测试对象m=1的所有属性列表为：\n',dir(m))
