#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：在Python中怎样编写一个基于计数器的循环？
答：可以使用while语句编写，并手动记录索引值，或者以for循环写成，使用range内置函数产生连续的整数偏移值。
'''

# 示例代码
X="good"

i=0
while i<len(X):
    print(X[i], end=' ')
    i+=1
print()

for i in range(len(X)):
    print(X[i], end=' ')
print()
