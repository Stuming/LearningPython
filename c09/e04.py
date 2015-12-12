#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
你可能使用什么模块把Python对象存储在文件中，而不需要亲自将它们转换成字符串？

答：pickle模块可以，而且不用刻意转换成字符串。struct模块也是类似的，但是需要将数据打包成为二进制格式，从而保存在文件中。

    其中， pickle模块中常用函数是
    1. pickle.dump(obj, file, protocol=None,)

    必填参数obj表示将要封装的对象，必填参数file表示obj要写入的文件对象，file必须以二进制可写模式打开，即“wb”，可选参数protocol表示告知pickler使用的协议，支持的协议有0,1,2,3，默认的协议是添加在Python 3中的协议3

    2. pickle.load(file,*,fix_imports=True, encoding="ASCII", errors="strict")

    必填参数file必须以二进制可读模式打开，即“rb”，其他都为可选参数

    3. pickle.dumps(obj)

    以字节对象形式返回封装的对象，不需要写入文件中

    4. pickle.loads(bytes_object)

    从字节对象中读取被封装的对象

    struct模块中最重要的三个函数是
    1.pack(fmt, v1, v2, ...)

    按照给定的格式(fmt)，把数据封装成字符串(实际上是类似于c结构体的字节流)

    2.unpack(fmt, string)

    按照给定的格式(fmt)解析字节流string，返回解析出来的tuple

    3.calcsize(fmt)

    计算给定的格式(fmt)占用多少字节的内存
"""
