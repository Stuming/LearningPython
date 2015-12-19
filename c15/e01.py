#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
在什么时候应该使用文档字符串而不是#字注释？

答：文档字符串（文件字符串）被认为最适用于较大型功能性的文档。用来描述程序中的模块、函数、类以及方法的使用。#号注释适用于较小功能的文档，最好只限于关于表达式或语句的微型文档。
    一方面因为文件字符串在源代码文件中比较容易找到，另一方面也是因为PyDoc系统能将其取出并显示。
'''


# Example

"""
举例说明，代码来自c09\e02.py
程序实现功能：修改元组中第一个元素。在此过程中，（4,5,6）应该变成（1,5,6）
"""

"""
利用切片合并的方法修改元组中元素
"""
T = (4,5,6)
T1 = (1,)+T[1:]  #切片合并
print("利用切片合并的方法修改：",T1)

"""
利用转换为列表的方法修改元组中的元素
"""
tmp = list(T)  #将元组转换为列表
tmp[0] = 1
T2 = tuple(tmp)  #将修改后的列表转换为元组
print("利用转换为列表的方法修改：",T2)
