#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：from语句和import语句有什么关系？
答：from语句和import语句都会导入整个模块，不同的是from语句会从被导入的模块中复制一个或多个变量到其所在的作用域中。
    from语句的这项功能可以让导入者直接使用被导入的变量名(name)，而不是像import语句导入那样通过模块来使用变量名(module.name)。
    一般来说，应该避免使用from语句而使用import语句，这样可以使程序更加易读，也可避免名称的冲突。
'''
