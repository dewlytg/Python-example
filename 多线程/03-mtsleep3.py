#!/usr/bin/env python
#coding:utf-8

"""
threading模块
我们应该避免使用thread模块，原因是它不支持守护线程。当主线程退出时，所有的子线程不论它们是否还在工作，都会被强行退出。有时我们并不期望这种行为，这时就引入了守护线程的概念。threading模块则支持守护线程。
"""
import threading
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec):
    print "start loop", nloop, "at:", ctime()
    sleep(nsec)
    print "loop", nloop, "done at:", ctime()

def main():
    print "starting at:", ctime()
    threads = []
    nloops = range(len(loops))

    ##创建线程
    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    ##开始线程
    for i in nloops:
        threads[i].start()

    ##等待所有结束线程
    for i in nloops:
        threads[i].join()

    print "all end:", ctime()

if __name__ == '__main__':
    main()

"""
start()         开始线程活动
join()          等待线程终止
　　所有的线程都创建了之后，再一起调用 start()函数启动，而不是创建一个启动一个。而且，不用再管理一堆锁（分配锁，获得锁，释放锁，检查锁的状态等），只要简单地对每个线程调用 join()函数就可以了。
join()会等到线程结束，或者在给了 timeout 参数的时候，等到超时为止。join()的另一个比较重要的方面是它可以完全不用调用。一旦线程启动后，就会一直运行，直到线程的函数结束，退出为止。

starting at: Thu Sep 07 17:28:21 2017
start loop 0 at: Thu Sep 07 17:28:21 2017
start loop 1 at: Thu Sep 07 17:28:21 2017
loop 1 done at: Thu Sep 07 17:28:23 2017
loop 0 done at: Thu Sep 07 17:28:25 2017
all end: Thu Sep 07 17:28:25 2017
"""