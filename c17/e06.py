#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码在Python3.x下的输出及原因？
答：输出'Spam'。因为nonlocal语句(Python3.x中可用)意味着在嵌套函数中对X赋值，以修改外围函数（the enclosing function）的本地作用域中的X。没有这条语句，这个赋值会把X当作是嵌套函数的本地变量，使它成为一个不同的变量，那么这段代码将会输出'NI'。 
'''

# 题设代码及验证

def func():
    X='NI'
    def nested():
        nonlocal X
        X='Spam'
    nested()
    print(X)

func()
