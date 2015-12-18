#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：在Python中怎样编写多路分支？
答：可以利用if...elif...else复合语句编写，也可以利用字典实现相同的效果
'''

# 示例代码
choice='c'

#if...elif...else
if choice=='a':
    print("age")
elif choice=='b':
    print("bug")
elif choice=='c':
    print("cut")
else:
    print("Bad choice")

#dictionary
branch={'a':"age",
        'b':"bug",
        'c':"cut"}
print(branch.get(choice,"Bad choice"))
