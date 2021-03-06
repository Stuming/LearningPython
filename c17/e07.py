#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：举出三种或四种Python函数中保存状态信息的方法。
答：函数返回的时候本地变量的值已经不在了，但可以使用共享的全局变量、嵌套函数对外围函数作用域的引用（enclosing function scope references within nested functions），或者使用默认参数值来让一个Python函数保持状态信息。
    函数属性有时候允许把状态附加到函数自身，而不是在作用域中查找。另一种替代方法，使用类机制，有时候比其他任何基于作用域的技术更好地支持状态，因为它使得属性赋值很明确。
'''
