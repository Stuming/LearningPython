#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
你怎么一次复制嵌套结构的所有组成部分？

答：导入copy模块，然后调用copy.deepcopy()。实际中浅层复制通常足以满足大多数要求，如aList[:]、aDict.copy()。
"""

#Example
import copy
L1=[1, 2, [3, 4]]
L2=copy.deepcopy(L1)
L3=L1.copy()

print("原本的L1:", L1)
print("L2, L3分别是L1的深层拷贝和浅层拷贝")
L2[2][0]=3.5
print("经L2[2][0]=3.5后的L1不变：", L1)
L3[2][0]=3.5
print("经L3[2][0]=3.5后的L1改变：", L1)
