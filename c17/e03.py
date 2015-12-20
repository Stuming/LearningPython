#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：题设代码输出及原因？
答：一行输出'NI',另一行输出'Spam'。函数中引用的变量会找到其本地变量，而在末尾的print中引用的变量会找到其全局变量。
'''

# 题设代码及验证

X='Spam'
def func():
    X='NI'
    print(X)

func()
print(X)
