#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：__getattr__和__getattribute__以及特性和描述符之间主要的功能区别是什么？
答：__getattr__和 __getattribute__方法更为通用：它们用来捕获任意多的属性。相反，每个特性或描述符只针对一个特定属性提供访问拦截——我们不能用单个的特性或描述符捕获每个属性获取。
    另一方面， 特性和描述符都通过设计来处理属性获取和赋值：__getattr__和__getattribute__只处理获取；要拦截赋值，必须编写__setattr__。实现也是不同的： __getattr__和__getattribute__是操作符重载方法，而特性和描述符是手动赋给类属性的对象。
'''
