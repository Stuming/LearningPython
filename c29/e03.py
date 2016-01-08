#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：如何在类中拦截分片操作？
答：分片由__getitem__索引方法拦截，它用一个分片对象调用。
'''

