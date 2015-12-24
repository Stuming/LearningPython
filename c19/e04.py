#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：什么是函数注解，如何使用它们？
答：函数注解是对函数的参数及其结果的语法上的修饰，在python3.0及其后的版本可用。
    注解会被收集到分配给函数__annotations__属性的一个字典中。Python在这些注解上没有放置语义含义，而是直接将其包装，以供其他工具潜在地使用。具体的使用方法见示例代码：
'''

# 示例代码
def func(a:'A', b:'B'=2)->"int": #冒号和右箭头后面的字符串分别是参数和return的注解
    print(a, b)
    return 1

print(func.__annotations__)
