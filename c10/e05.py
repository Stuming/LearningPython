#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：怎么在单个行上编写复合语句？
答：复合语句的主体可以移到开头行的冒号后面，但前提是主体只由非复合语句构成。
错误形式如：
1、if test1: if test2:print(x)  if 后面有 else 子句的话，会导致语义不明确
2、if x < y < z: print(x); print(y); print(z)  分号的优先级比冒号的高，要么所有的 print() 方法都会被执行，要么所有方法都不会被执行
'''

# 示例代码
from functools import reduce
if True:print(reduce(lambda x,y:x*y,range(1,101))) # 实现100的阶乘
