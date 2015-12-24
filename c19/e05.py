#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：什么是递归函数，如何使用它们？
答：递归函数是指直接或间接地调用自身以进行循环的函数。
    它可以用来遍历拥有任意的、不可预知的形状的结构。甚至是简单循环和迭代的替换，但不一定是最简单或最高效的。
'''

# 示例代码
def func(X):
 return 0 if not X else X[0]+func(X[1:])

print(func(range(5)))
