#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
Python在什么时候会认为一个对象为真？

答：如果对象为非零数字，或者非空集合体对象，就被认为是真。内置的True、False关键字可以认为是预先定义的整数1和0。
"""

#Example
temp1 = 1
temp2 = 0
temp3 = [1,2,3]
temp4 = []
bool1 = bool(temp1)
bool2 = bool(temp2)
bool3 = bool(temp3)
bool4 = bool(temp4)
print ("temp1 = 1:",bool1)
print ("temp2 = 0:",bool2)
print ("temp3 = [1,2,3]:",bool3)
print ("temp4 = []:",bool4)
