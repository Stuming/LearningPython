#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：思考下面三条语句，它们会改变A的值吗？
    A = ["spam"]
    B = A
    B[0] = "shrubbery"
答：会，A最后会输出["shrubbery"]。因为列表是可变对象，可以进行在原处的修改，A和B共同指向的对象的内容经过对B的索引的赋值被改变了，因此A的值自然就变了
'''

#代码验证：
A = ["spam"]
print("A = [\"spam\"], A's value is %s"% A)
B = A
print("B = A, A's value is %s"% A)
B[0] = "shrubbery"
print("B[0] = \"shrubbery\", A's value is %s"% A)

