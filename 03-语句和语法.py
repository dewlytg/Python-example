#coding:utf-8

#Python语句中有一些基本规则和特殊字符：
"""
井号(#)表示之后的字符为 Python 注释
换行 (\n) 是标准的行分隔符（通常一个语句一行）
反斜线 ( \ ) 继续上一行
分号 ( ; )将两个语句连接在一行中
冒号 ( : ) 将代码块的头和体分开
语句（代码块）用缩进块的方式体现
不同的缩进深度分隔不同的代码块
Python 文件以模块的形式组织
"""

print #this is a comment line

print "abc" + "\n"

print "abc" \
"efg"

if True:
    print "abc"

import sys; x = 'foo'; sys.stdout.write(x + '\n')