#!/usr/bin/env python

"""
线程之间支持数据共享，不用传递q，直接调用q即可
进程之间不支持数据共享，必须传递q，相当于复制了一个q给子进程
"""
# import threading,queue
#
# def f():
#     q.put(["42,None,bob"])
#
# if __name__ == "__main__":
#     q = queue.Queue()
#     t = threading.Thread(target=f,)
#     t.start()
#     print(q.get())
#     t.join()

from multiprocessing import Process,Queue

def f(q):
    q.put("[42,None,bob]")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()

