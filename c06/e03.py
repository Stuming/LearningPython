#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：这样如何，A会改变吗？
    A = ["spam"]
    B = A[:]
    B[0] = "shrubbery"
答：不会，A的值为["spam"]。分片表达式会在给B赋值前创建一份拷贝，因此第二条赋值语句后A和B指向的对象的值相同，但是是不同对象，因此第三条赋值语句对A及A指向的对象没有影响。
'''

#代码验证：
A = ["spam"]
print("A = [\"spam\"], A's value is %s"% A)
B = A[:]
print("B = A[:], A's value is %s"% A)
B[0] = "shrubbery"
print("B[0] = \"shrubbery\", A's value is %s"% A)

