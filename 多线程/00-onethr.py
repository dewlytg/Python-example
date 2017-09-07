#!/usr/bin/env python

"""
单线程,在单线程中顺序执行两个循环。一定要一个循环结束后，另一个才能开始。总时间是各个循环运行时间之和
"""

from time import sleep,ctime

def loop0():
    print "start loop 0 at:",ctime()
    sleep(4)
    print "loop 0 done at: ",ctime()

def loop1():
    print "start loop1 at:",ctime()
    sleep(2)
    print "loop 1 done at: ",ctime()

def main():
    print "starting at:",ctime()
    loop0()
    loop1()
    print "all DONE at:",ctime()

if __name__ ==  "__main__":
    main()

"""
starting at: Thu Sep  7 15:32:15 2017
start loop 0 at: Thu Sep  7 15:32:15 2017
loop 0 done at:  Thu Sep  7 15:32:19 2017
start loop1 at: Thu Sep  7 15:32:19 2017
loop 1 done at:  Thu Sep  7 15:32:21 2017
all DONE at: Thu Sep  7 15:32:21 2017

"""