#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：如何以一种特定的编码格式创建一个Unicode文本文件？
答：要以特定编码格式创建一个Unicode文本文件，可以把想要的编码名称传递给Python 3.0中的内置函数open()（在Python 2.6中是codecs.open()）。当字符串写入文件中的时候，将会按照每个想要的编码方式来进行编码。
    也可以手动把一个字符串编码为字节，并在二进制模式下将其写入。但是，这通常需要额外的工作。
'''