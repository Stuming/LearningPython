#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：哪两种运算符重载方法可以用来支持类中的迭代？
答：__getitem__和__iter__方法可以用来支持类中的迭代。
    Python首先尝试使用__iter__，如果没有搜索到，则会使用__getitem__方法。
'''
