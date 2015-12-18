#! /usr/bin/python3
# -*- coding:utf8 -*-

'''
问：break和continue之间有何区别？
答：break会立即结束当前循环，而continue是跳回到循环的顶部（跳转到while中测试之前的部分或for中的下一次元素获取）
'''

# 示例代码
while True:
    print("break结束无限循环")
    break

for i in "a bc":
    if i==' ':
        continue
    print(i, end='')

print()
