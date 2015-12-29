#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：在什么情况下必须通过import而不能通过from使用包？
答：只有在需要读取定义在一个以上路径的相同变量名和使用reload调用时，必须通过import使用包，而不能使用from。
    使用import，路径可让引用独特化，from却让任何变量名在作用域内只有一个版本。
'''
