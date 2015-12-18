#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：一个循环的else分句何时执行？
答：在循环结束时执行一次（前提是循环结束的原因不是因为break）
'''

# 示例代码
for i in range(5):
    break
else:
    print("no break1")

for i in range(5):
    pass
else:
    print("no break2")
