#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
for循环和迭代器之间有什么关系？

答：for循环本身会使用迭代协议来遍历迭代对象中的每一项。for循环会在每次迭代中调用该对象的__next__()方法，而且会捕捉由__next__()引发的内置StopIteration异常，从而决定是否停止循环。
'''
