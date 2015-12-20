#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：一行输出'NI',另一行输出'Spam'。因为嵌套函数中的print语句会在所在的函数本地作用域中发现这个变量名，而末尾的print会在全局作用域中发现这个变量名。
'''

# 题设代码及验证

X='Spam'
def func():
    X='NI'
    def nested():
        print(X)
    nested()

func()
print(X)
