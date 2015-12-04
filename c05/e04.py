#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：通过什么工具你可以找到一个数字的平方根以及它的平方？
答：至少可以通过math模块，内置函数pow()以及指数表达式三种方法。
'''

#代码验证：
import math
X=2

print("下面是三种方法求X的平方根的结果")
print(math.sqrt(X))
print(pow(X,0.5))
print(X**0.5)
print("下面是三种方法求X的平方的结果")
print(math.pow(X,2))
print(pow(X,2))
print(X**2)

input() # 控制台下显示才使用这行，防止一闪而过看不到执行结果
