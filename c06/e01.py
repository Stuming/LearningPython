#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：思考下面三条语句，它们会改变A打印出的值吗？
    A = "spam"
    B = A
    B = "shrubbery"
答：不会，A的值为"spam"。对A赋值为字符串"spam"后，只是在对B进行新的字符串赋值，对A的值没有进行修改，对字符串"spam"也没有进行修改。
'''

#代码验证：
A = "spam"
print("A = \"spam\", A's value is %s"% A)
B = A
print("B = A, A's value is %s"% A)
B = "shrubbery"
print("B = \"shrubbery\", A's value is %s"% A)

