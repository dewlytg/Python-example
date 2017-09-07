#!/usr/bin/env python
#coding:utf-8

"""
试用可调用的类
"""
import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc (object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func,self.args)

def loop(nloop, nsec):
    print "start loop", nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        ##调用ThreadFunc实例化的对象，创建所有线程
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    ##开始线程
    for i in nloops:
        threads[i].start()

    ##等待所有结束线程
    for i in nloops:
        threads[i].join()

    print 'all end:', ctime()

if __name__ == '__main__':
    main()


"""
创建新线程的时候，Thread 对象会调用我们的ThreadFunc 对象，这时会用到一个特殊函数__call__()。由于我们已经有了要用的参数，所以就不用再传到 Thread()的构造函数中。由于我们有一个参数的元组，这时要在代码中使用 apply()函数。

我们传了一个可调用的类(的实例)，而不是仅传一个函数。
__init__()

方法在类的一个对象被建立时运行。这个方法可以用来对你的对象做一些初始化。
apply()

apply(func [, args [, kwargs ]]) 函数用于当函数参数已经存在于一个元组或字典中时，间接地调用函数。args是一个包含将要提供给函数的按位置传递的参数的元组。如果省略了args，任何参数都不会被传递，kwargs是一个包含关键字参数的字典。
apply() 用法：
#不带参数的方法
>>> def say():
    print 'say in'

>>> apply(say)
say in

#函数只带元组的参数
>>> def say(a,b):
    print a,b

>>> apply(say,('hello','虫师'))
hello 虫师

#函数带关键字参数
>>> def say(a=1,b=2):
    print a,b

    
>>> def haha(**kw):
    apply(say,(),kw)

>>> haha(a='a',b='b')
a b

starting at: Thu Sep 07 18:15:43 2017
start loop 0 at: Thu Sep 07 18:15:43 2017
start loop 1 at: Thu Sep 07 18:15:43 2017
loop 1 done at: Thu Sep 07 18:15:45 2017
loop 0 done at: Thu Sep 07 18:15:47 2017
all end: Thu Sep 07 18:15:47 2017
"""