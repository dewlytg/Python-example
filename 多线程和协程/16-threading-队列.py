#!/usr/bin/env python

import threading,time
import queue

q = queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头",count)
        count += 1
        time.sleep(0.1)

def Consumer(name):
    while True:
        print("[%s] 取到 [%s] 并且吃了它..."%(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args=("zhangsan",))
c = threading.Thread(target=Consumer,args=("lisi",))
c1 = threading.Thread(target=Consumer,args=("wangwu",))

p.start()
c.start()
c1.start()