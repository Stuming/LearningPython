#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：怎么使用print语句来向外部文件发送文本？
答：要把一个单个的打印操作打印到一个文件，可以使用Python 3.x的print(X,file=F)调用形式，Python 2.6的扩展的print >> file，X语句形式，或者再打印前把sys.stout指定为手动打开的文件并在之后恢复最初的值。
'''

# 示例代码
log=open('log.txt','w') # 创建log.txt 可读写
print(1,2,3,file=log)   # 向log发文本
log.close()
print(open('log.txt').read())
