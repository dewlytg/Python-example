#!/usr/bin/env python
#coding:utf-8

import thread
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec,lock):
    print "start loop", nloop, "at:", ctime()
    sleep(nsec)
    print "loop", nloop, "done at:", ctime()
    ##解锁
    lock.release()

def main():
    print "starting at:", ctime()
    locks = []
    ##以loops数组创建列表，并赋值给nloops
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        ##锁定
        lock.acquire()
        ##追加到locks[]数组中
        locks.append(lock)

    ##执行多线程
    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print "all end:", ctime()

if __name__ == '__main__':
    main()

"""
我们先调用 thread.allocate_lock()函数创建一个锁的列表，并分别调用各个锁的 acquire()函数获得锁。获得锁表示“把锁锁上”。锁上后，我们就把锁放到锁列表 locks 中。
下一个循环创建线程，每个线程都用各自的循环号，睡眠时间和锁为参数去调用 loop()函数。为什么我们不在创建锁的循环里创建线程呢？有以下几个原因：(1) 我们想到实现线程的同步，所以要让“所有的马同时冲出栅栏”。(2) 获取锁要花一些时间，如果你的线程退出得“太快”，可能会导致还没有获得锁，线程就已经结束了的情况。
在线程结束的时候，线程要自己去做解锁操作。最后一个循环只是坐在那一直等（达到暂停主线程的目的），直到两个锁都被解锁为止才继续运行。

starting at: Thu Sep 07 17:07:04 2017
start loop 0 at:start loop  Thu Sep 07 17:07:04 20171
 at: Thu Sep 07 17:07:04 2017
loop 1 done at: Thu Sep 07 17:07:06 2017
loop 0 done at: Thu Sep 07 17:07:08 2017
all end: Thu Sep 07 17:07:08 2017
"""