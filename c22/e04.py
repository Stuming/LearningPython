#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：什么时候必须使用import，不能使用from？
答：当需要读取两个不同模块中的相同变量名时，就必须使用import，而不能使用from；因为必须指定变量名所在模块，从而保证这两个变量名(如 module1.name和module2.name)是独特的。
'''
