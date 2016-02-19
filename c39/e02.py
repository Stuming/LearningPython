#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
如何声明一个类的元类？

答：python 3.X：在类标题栏使用关键字属性："class C(metaclass = M):"
        继承超类也可以列在标题中，在元类之前："class C(E, metaclass = M):"
    python 2.X: 使用类属性："__metaclass__ = M"
"""