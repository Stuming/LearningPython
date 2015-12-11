#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
Python在什么时候会认为一个对象为真？

答：如果对象为非零数字，或者非空集合体对象，就被认为是真。内置的True、False关键字可以认为是预先定义的整数1和0。
"""

#Example
print ("bool(1):",bool(1))
print ("bool(0):",bool(0))
print ("bool([1, 2, 3]):",bool([1, 2, 3]))
print ("bool([]):",bool([]))
