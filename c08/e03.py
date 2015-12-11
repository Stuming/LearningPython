#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：举出四种在原处修改列表对象的运算。
答：这里给出四种：1.对索引的赋值；2.元素插入方法；3.列表翻转方法；4.元素添加方法。另，可用切片、排序、pop()、del等实现
'''

#代码验证：
L=[1, 3, 5]
print("列表的初始值：", L)
print("列表对象的初始内存地址为：",id(L))

L[2]=4
print("经L[2]=4修改后：", L)
print("经L[2]=4修改后内存地址为：",id(L))

L.insert(1, 2)
print("经L.insert(1, 2)修改后：", L)
print("经L.insert(1, 2)修改后内存地址为：",id(L))

L.reverse()
print("经L.reserve()修改后：", L)
print("经L.reserve()修改后内存地址为：",id(L))

L.append(0)
print("经L.append(0)修改后：", L)
print("经L.append(0)修改后内存地址为：",id(L))

L[2:4]=[2,3]
print("经L[2:4]=[2,3]修改后：", L)
print("经L[2:4]=[2,3]修改后内存地址为：",id(L))

L.sort()
print("经L.sort()修改后：", L)
print("经L.sort()修改后内存地址为：",id(L))

L.pop(0)
print("经L.pop(0)修改后：", L)
print("经L.pop(0)修改后内存地址为：",id(L))

del L[3]
print("经del L[3]修改后：", L)
print("经del L[3]修改后内存地址为：",id(L))

