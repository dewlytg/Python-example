#!/usr/bin/env python

import threading
import time

lock = threading.Lock() #定义一个锁
num = 0
t_objs = []  #存线程实例

def run(n):
    lock.acquire()
    global num
    num += 1
    lock.release()

for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_objs.append(t)  #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

for t in t_objs:  #循环线程实例列表，等待所有线程执行完毕
    t.join()

print("all threads has finished...", threading.current_thread())
print("num:", num)