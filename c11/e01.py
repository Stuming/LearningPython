#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：举出三种可以把三个变量赋值成相同值的方式
答：将三个变量赋值成相同的值：
   1、使用多重目标赋值语句(A=B=C=0)
   2、序列赋值语句(A,B,C=0,0,0)
   3、单独行上的赋值语句(A=0;B=0;C=0)
'''

# 示例代码
a=b=c=0
print("a,b,c值分别为：",a,b,c,"\n即a=b=c=0将a,b,c赋值为同一个值：",a)
a,b,c=1,1,1
print("a,b,c值分别为：",a,b,c,"\n即(a,b,c=1,1,1)将a,b,c赋值为同一个值：",a)
a=2;b=2;c=2
print("a,b,c值分别为：",a,b,c,"\n即(a=2;b=2;c=2)将a,b,c赋值为同一个值：",a)
