#!/usr/bin/env python
import threading, time

def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    print('-----between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)

num, num2 = 0, 0
lock = threading.RLock()
for i in range(10):
    t = threading.Thread(target=run3)
    t.start()

while threading.active_count() != 1: #此while循环等同于join，主线程等待子线程执行完成后执行else中代码
    print(threading.active_count())
    print("ok")
else:
    print('----all threads done---')
    print(num, num2)