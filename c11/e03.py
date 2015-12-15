#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：L=L.sort()有什么错误？
答：列表的sort方法就像append方法，也是对主体列表进行在原处修改：返回None，而不是其修改的列表。赋值给L，会把L设为None，而不是排序后的列表。
   新的内建函数sorted会排序任何序列并传回具有排序结果的新列表因为着并不是在原处修改，将其结果赋值给变量名，是可以的。
'''

# 示例代码
L=[3,5,2,7,4,8,9,10]
print("原列表L为：",L)
L.sort()    # 在原处修改
print("经L.sort()处理后L：",L)
L=L.sort()
print("经L=L.sort()处理后L：",L)
M=[3,5,2,7,4,8,9,10]
print("原列表M为：",M)
N=sorted(M)   # 不在原处修改
print("经N=sorted(M)处理后M、N分别为：",M,N)
