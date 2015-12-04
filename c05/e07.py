#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：怎样将一个整数转换为浮点数？
答：可以用内置的float()函数；也可以用混合类型表达式混合整数和浮点数的方法；还可以利用python3.0的真除法得到浮点数，因为真除法总是返回一个浮点数结果。
'''

#代码验证：
X=2

print("float(X):%s, type:%s" % (float(X), type(float(X))))
print("(X+0.0):%s, type:%s" % (X+0.0, type(X+0.0)))
print("(X/1):%s, type:%s" % (X/1, type(X/1)))

input() # 控制台下显示才使用这行，防止一闪而过看不到执行结果
