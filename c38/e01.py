#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
1.正如本章的提示中提到的，我们在本章“添加装饰器参数”小节所编写的带有装饰器参数的计时器函数装饰器，
只能应用于简单函数，因为它使用了一个嵌套的类，该类带有一个__call__运算符重载方法来捕获调用。这种
结构对于类方法无效，因为装饰器实例传递给self，而不是主体类实例。
    重新编写这个装饰器，以便它可以应用于简单函数和类方法，并且在函数和方法上都测试它。
    注意，我们可以使用赋值函数对象属性来记录总的时间，因为你没有一个嵌套的类用于状态保持，并且不能
从装饰器代码的外部访问非局部变量。
"""

import time
def timer(label='', trace=True): # On decorator args: retain args
    def onDecorator(func): # On @: retain decorated func
        def onCall(*args, **kargs): # On calls: call original
            start = time.clock() # State is scopes + func attr
            result = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed # 赋值函数的对象属性，用于替代self.alltime
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator

# 函数测试

@timer(trace=True, label='[CCC]==>')
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

for func in (listcomp, mapcall):
    result = func(5)
    func(5000000) # 运行但没有print返回值，只是记录了运行时间
    print(result) # 显示func(5)的返回值
    print('allTime = %s\n' % func.alltime) # 显示运行的总时间

# 方法测试

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @timer()
    def giveRaise(self, percent): # giveRaise = timer()(giveRaise)
        self.pay *= (1.0 + percent)
	
    @timer(label='**')
    def lastName(self): # lastName = timer(...)(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10) # 会输出giveRaise的运行时间
sue.giveRaise(.20)
print(bob.name, ': ', bob.pay)
print(sue.name, ': ', sue.pay)
print(bob.lastName())
print(sue.lastName())
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))