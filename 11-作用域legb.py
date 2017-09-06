#!/usr/bin/env python
#coding:utf-8

"""
简而言之，LEGB 代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__
    locals 是函数内的名字空间，包括局部变量和形参
    enclosing 外部嵌套函数的名字空间（闭包中常见）
    globals 全局变量，函数定义所在模块的名字空间
    builtins 内置模块的名字空间
所以，在 Python 中检索一个变量的时候，优先回到 locals 里面来检索，检索不到的情况下会检索 enclosing ，enclosing 没有则到 globals 全局变量里面检索，最后是到 builtins 里面来检索。
当然，因为 builtins 的特殊性，我们可以直接在 builtins 里面添加变量，这样就可以在任意模块中访问变量，不过这种方法太过于变态，不推荐这么做。
__builtins > globals > encloseing function > locals
"""


import __builtin__
__builtin__.a_var = "builtins"
print a_var

a_var = "global value"
print a_var

def outer():
    a_var = "enclosing value"
    print a_var
    def inner():
        a_var = "local value"
        print a_var
    inner()
    print a_var

outer()