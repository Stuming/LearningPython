#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：try语句是用来做什么的？
答：try语句是用于在Python脚本中捕捉和恢复异常(错误)的，这是程序中自行检查错误的方法之一。
'''

# 示例代码
s=input("input your age:")
if s=="":
    raise Exception("input must not be empty.")  # raise抛出一个指定的异常
try:                                             # 执行try子句，如果没有异常发生，忽略except子句，try执行后结束
    i=int(s)
except Exception as err:                         # 如果在执行try子句中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
    print(err)
finally:                                         # 无论在任何情况下都会执行的清理行为
    print("Goodbye!")

