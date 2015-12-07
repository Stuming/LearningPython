#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：思考下面三条语句，它们会改变A打印出的值吗？
    A = "spam"
    B = A
    B = "shrubbery"
答：不会，A的值仍为"spam"。A和B最初共享(即引用)了同一个字符串对象“spam”，但两个变量名在命名空间里并没有什么关联，所以当B赋值为字符串“shrubbery”时，只是B被重新设置为指向了新的字符串对象，对A没有影响；此外，不可能在原处修改字符串，因为字符串是不可变对象。
'''

#代码验证：
A = "spam"
print("A = \"spam\", A's value is %s"% A)
B = A
print("B = A, A's value is %s"% A)
B = "shrubbery"
print("B = \"shrubbery\", A's value is %s"% A)

