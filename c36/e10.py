#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：Python 3.0的字符串类型修改对你的代码有多大的影响？
答：Python 3.0的字符串类型修改的影响， 取决于你所使用的字符串的类型。
    对于那些使用简单ASCII文本的脚本，可能根本没有影响：在此情况下，str字符串类型在Python 2.6和Python 3.0中的用法相同。
    此外，尽管标准库中像re、 struct、 pickle和xml这样字符串相关的工具可能在Python 3.0和Python 2.6中技术上的用法不同，但这一修改很大程度上与大多数程序不相关。
	因为Python 3.0的str和bytes以及Python 2.6的str都支持几乎相同的接口。如果你处理非ASCII的Unicode数据， 只需要直接把Python 2.6的工具集unicode和codecs.open()转换为Python 3.0的str和open。
	如果是处理二进制数据文件，将需要处理的数据作为bytes或bytearray对象的内容。由于它们与Python 2.6字符串具有相似的接口， 所以影响再次变得很小。
'''