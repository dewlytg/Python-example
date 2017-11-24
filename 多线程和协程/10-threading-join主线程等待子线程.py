#!/usr/bin/env python

import threading
import time

t_lists = []
start_time = time.time()

def run(n):
    print("task",n)
    time.sleep(2)
    print("task done...",n,threading.current_thread())

for i in range(50):
    t = threading.Thread(target=run,args=("t-%d" %i,))
    t.start()
    t_lists.append(t)

for t in t_lists:
    t.join() # 主线程等待所有子线程运行，子线程并行，主线程和子线程是串行

end_time = time.time()
print("main threading has done",threading.current_thread())
print(end_time - start_time)