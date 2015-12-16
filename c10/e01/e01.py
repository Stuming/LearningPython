#! /usr/bin/python3
# -*- coding:utf8 -*-

def max(a,b):
    "比较两数a，b的大小并输出"
    
    if a<b:
        return b
    return a

print("请分别输入整数a,b：")
a=input("a=")
b=input("b=")
print("%s与%s中最大值为："%(a,b),max(a,b))

