#!/usr/bin/env python
#coding:utf-8

"""
为了让 mtsleep5.py 中，Thread 的子类更为通用，我们把子类单独放在一个模块中，并加上一
个 getResult()函数用以返回函数的运行结果。
"""

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print "starting",self.name,"at:",ctime()
        self.res = apply(self.func,self.args)
        print self.name,"finished at:",ctime()