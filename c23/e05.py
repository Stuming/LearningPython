#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：from mypkg import spam和from . import spam有什么差别？
答：1、from mypkg import spam是绝对导入：mypkg的搜索跳过包路径并且mypkg位于sys.path中的一个绝对目录中。
    2、from . import spam是相对导入：spam的查找是相对于该语句所在的包。

补充理解：
    绝对导入：指明package名。比如 import a，Python 会跳过导入语句所在包目录而直接在sys.path里寻找名为a的模块。
    相对导入：默认的导入搜索路径定义为导入语句所在文件的包路径，比如一个 package 下有 a.py 和 b.py 两个文件，在 a.py 里 from . import b 即是相对导入 b.py。
'''
