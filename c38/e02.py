#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
2.我们在本章中编写的Public/Private类装饰器将会为一个装饰的类中的每次属性获取增加负担。
尽管我们可以直接删除@装饰行以获取速度，但我们也可以扩展装饰器自身类检查__debug__开关，
并且在命令行传递-O Python标志的时候根本不执行包安装。通过这种方法，我们可以加速程序而
不用修改源代码，即通过命令行参数（python -O main.py）。编写代码并测试这一扩展。
'''

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance:
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)
                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)
                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

# 测试代码

@Private('age') # Person = Private('age')(Person)
class Person: # Person = onInstance with state
    def __init__(self, name, age):
        self.name = name
        self.age = age

X = Person('Bob', 40)
print(X.name)
X.name = 'Sue'
print(X.name)
# print(X.age) # 需要使用"python -O main.py"命令运行，不然报错：TypeError: private attribute fetch: age
# X.age = 999 # 同上
# print(X.age) # 同上

@Public('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

X = Person('bob', 40)
print(X.name)
X.name = 'Sue'
print(X.name)
# print(X.age) # FAILS unless "python -O main.py"
# X.age = 999 # 同上
# print(X.age) # 同上