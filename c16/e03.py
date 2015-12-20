#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：当一个函数没有return语句时，它将返回什么？
答：如果控制流在函数主体末尾没有遇到return语句，函数就会传回None对象，这类函数通常是通过表达式语句调用的。
'''

# Example

def func():
    pass

print("函数主体中没有return语句时其返回：\n",func())
