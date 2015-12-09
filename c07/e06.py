#! /usr/bin/python3.4
# -*- coding:utf8 -*-

'''
字符串"a\nb\x1f\000d"之中有多少字符？
题设字符串有6个字符，其包含字符a、新行(\n)、字符b、二进制值31(十六进制转义\x1f)、二进制值0(八进制转义\000)及字符d。可用内置函数len()验证，可用ord()查看每个字符的ASCII编码，从而得出实际的字节值。
'''

# 代码验证：
S = "a\nb\x1f\000d"
print("字符串\"a\\nb\\x1f\\000d\"中字符数：",len(S))
print("字符串\"a\\nb\\x1f\\000d\"子字符及对应的ASCII码依次为：")
for k in range(len(S)):
    print(S[k],ord(S[k]))  #显示子字符及ASCII码
