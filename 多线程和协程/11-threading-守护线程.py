#!/usr/bin/env python

import threading
import time

start_time = time.time()

def run(n):
    print("task",n)
    time.sleep(2)
    print("task has done...",n,threading.current_thread())

for i in range(50):
    t = threading.Thread(target=run,args=("t-%d" %i,))
    t.setDaemon(True) #设置当前线程为守护线程，主线程不等待其他线程，执行完成就退出，相当于线程放在后台执行，"&"
    t.start()

print("main threading has done.",threading.current_thread())
end_time = time.time()
print("cost:",end_time - start_time)
