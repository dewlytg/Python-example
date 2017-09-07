#!/usr/bin/env python

import thread
from time import sleep,ctime

def loop0():
    print "start loop 0 at:",ctime()
    sleep(4)
    print "loop 0 done at:",ctime()

def loop1():
    print "start loop 1 at:",ctime()
    sleep(2)
    print "loop 1 done at:",ctime()

def main():
    print "starting at:",ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print "all DONE at:",ctime()

if __name__ == '__main__':
        main()

"""
starting at: Thu Sep  7 15:31:07 2017
start loop 0 at: Thu Sep  7 15:31:07 2017
start loop 1 at: Thu Sep  7 15:31:07 2017
loop 1 done at: Thu Sep  7 15:31:09 2017
loop 0 done at: Thu Sep  7 15:31:11 2017
all DONE at: Thu Sep  7 15:31:13 2017


这个程序的输出与之前的输出大不相同，之前是运行了 6，7 秒，而现在则是 4 秒，是最长的循
环的运行时间与其它的代码的时间总和。

睡眠 4 秒和 2 秒的代码现在是并发执行的。这样，就使得总的运行时间被缩短了。你可以看到，
loop1 甚至在 loop0 前面就结束了。程序的一大不同之处就是多了一个“sleep(6)”的函数调用。为
什么要加上这一句呢？因为，如果我们没有让主线程停下来，那主线程就会运行下一条语句，显示
“all done”，然后就关闭运行着 loop0()和 loop1()的两个线程，退出了。
我们没有写让主线程停下来等所有子线程结束之后再继续运行的代码。这就是我们之前说线程
需要同步的原因。在这里，我们使用了 sleep()函数做为我们的同步机制。我们使用 6 秒是因为我们
已经知道，两个线程（你知道，一个要 4 秒，一个要 2 秒）在主线程等待 6 秒后应该已经结束了。
你也许在想，应该有什么好的管理线程的方法，而不是在主线程里做一个额外的延时 6 秒的操
作。因为这样一来，我们的总的运行时间并不比单线程的版本来得少。而且，像这样使用 sleep()
函数做线程的同步操作是不可靠的。如果我们的循环的执行时间不能事先确定的话，那怎么办呢？
这可能造成主线程过早或过晚退出。这就是锁的用武之地了。
上一次修改程序，我们去掉了loop函数，现在，我们要再一次修改程序为例18.3的mtsleep2.py，
引入锁的概念。运行它，我们看到，其输出与 mtsleep1.py 很相似，唯一的区别是我们不用为线程
什么时候结束再做额外的等待。使用了锁，我们就可以在两个线程都退出后，马上退出。
"""