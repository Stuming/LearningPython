#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：表达式1+2.0+3的结果是什么类型？
答：是浮点型，因为在计算数值的时候，python会把混合类型表达式中的其它类型升级成表达式中最复杂的类型，然后用这种类型的运算法则进行运算。
'''

#代码验证：
print(type(1+2.0+3))