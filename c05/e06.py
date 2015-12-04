#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：怎样能够截断或舍去浮点数的小数部分？
答：用int()函数和math模块的trunc()方法可以截断小数部分；而round()方法是做四舍五入；math模块的floor()方法是舍去小数部分而得到离原数值最近且小于原数值的整数。
'''

#代码验证：
import math
X=-1.141

print("int(X):%f" % int(X))
print("math.trunc(X):%f" % math.trunc(X))
print("round(X):%f" % round(X))
print("math.floor(X):%f" % math.floor(X))

input() # 控制台下显示才使用这行，防止一闪而过看不到执行结果
