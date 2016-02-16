#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：为什么把ASCII文本看做是一种Unicode文本？
答：因为其7位范围值只是大多数Unicode编码的一个子集。
    例如，有效的ASCII文本也是有效的Latin-1文本（ Latin-1只是把一个8位字节中其余可能的值分配给额外的字符），并且是有效的UTF-8文本（ UTF-8为表示更多的字符定义了一个变量-字节方案，但是ASCII字符仍然用同样的代码表示,即单个的字节）。
	将ASCII文本看成是一种Unicode文本也使得Unicode能反向兼容世界上大量的ASCII文本。
'''
