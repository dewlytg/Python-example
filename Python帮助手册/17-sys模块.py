#coding:utf-8

import sys

#sys.argv[0]代表程序本身，sys.argv[1]代表第一个参数，以此类推
##获取程序名字
print "The name of this program is: %s" %(sys.argv[0])

##获取参数列表
print "The commnd line arguments are:"
for i in sys.argv:
    print i

##统计参数个数
print "There are %s arguments." %(len(sys.argv) -1)

##显示系统平台
print sys.platform

##path是一个目录列表，供Python从中查找第三方扩展模块。在python启动时，sys.path根据内建规则、PYTHONPATH变量进行初始化。
print sys.path

##内建模块的名字
print sys.builtin_module_names

def find_module(module):
    if module in sys.builtin_module_names:
        print module," => ","__builtin__"
    else:
        print module," => ",__import__(module).__file__

find_module("os")
find_module("sys")
find_module("strop")
find_module("zlib")
find_module("string")

##调用sys.exit(n)可以中途退出程序，当参数非0时，会引发一个SystemExit异常，从而可以在主程序中捕获该异常。
print "running..."

try:
    sys.exit(2)
except SystemError:
    print "SystemExit exit 1"

print "exited"