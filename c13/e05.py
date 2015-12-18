#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：怎样使range用于for循环中？
答：可以使用range和for的组合的常见场合就是在循环中遍历列表，并根据需要对其进行修改（也可以不做修改）。
'''

# 示例代码
L=[1, 2, 3]
print("修改前：", L)

for i in range(len(L)):
    L[i]+=1
print("修改后：", L)
