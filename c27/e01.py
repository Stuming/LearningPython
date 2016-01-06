#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
当我们从shelve获取一个Manager对象并打印它的时候，显示格式逻辑来自何处？

答：从单独的classtools模块的AttrDisplay继承其__str__打印模块。由于Manager本身没有打印方法，因此需要向上查找，直到在AttrDisplay中找到__str__。
"""