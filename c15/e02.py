#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
举出3种查看文档字符串的方式

答：打印对象的__doc__属性，调用PyDoc的help函数，利用PyDoc的GUI接口，将报表通过html网页格式呈现。
'''

# Example

import e04
print(e04.__doc__)  #只显示文档字符串，不显示 # 字注释
