#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：在Python 3.0中， 如何把非ASCII Unicode字符编写到字符串中？
答：非ASCII Unicode字符可以以十六进制转义（\xNN）和Unicode转义（\uNNNN, \UNNNNNNNN）编写到一个字符串中。
    在某些键盘上，一些非ASCII字符——例如，某些Latin-1字符，也可以直接录入。
'''