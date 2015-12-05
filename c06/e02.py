#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：思考下面三条语句，它们会改变A的值吗？
    A = ["spam"]
    B = A
    B[0] = "shrubbery"
答：会，A最后会输出["shrubbery"]。A和B共同指向的对象的内容经过B被改变了，因此A指向的结果也会发生变化。总的来说，列表是可变的。
'''

#代码验证：
A = ["spam"]
print("A = [\"spam\"], A's value is %s"% A)
B = A
print("B = A, A's value is %s"% A)
B[0] = "shrubbery"
print("B[0] = \"shrubbery\", A's value is %s"% A)

