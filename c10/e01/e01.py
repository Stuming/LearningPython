#! /usr/bin/python3
# -*- coding:utf8 -*-

def max(a,b):
    "比较两数a，b的大小并输出"
    max=a
    if max<b:
        max=b
    return max

print("请分别输入整数a,b：")
a=input("a=")
b=input("b=")
print("%s与%s中最大值为："%(a,b),max(a,b))

