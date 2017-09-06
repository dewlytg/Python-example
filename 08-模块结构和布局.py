#/usr/bin/env python
"this is a test module"


"""
# (1) 起始行(Unix)
# (2) 模块文档                             
# (3) 模块导入
# (4) 变量定义
# (5) 类定义
# (6) 函数定义
# (7) 主程序
"""

import sys
import os

debug = True

class FooClass(object):
    "Foo Class"
    pass

def test():
    "test function"
    foo = FooClass()

    if debug:
        print "ran test()"

if __name__ == "__main__":
    test()