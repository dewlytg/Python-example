#!/usr/bin/env python

from multiprocessing import Process,Pool
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i + 100

def Bar(arg):
    print("--->exec done:",arg,os.getpid())

if __name__ == "__main__":
    pool = Pool(3) #允许进程池同时放入3个进程
    print("main process",os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar) #callback=回调
        #pool.apply(func=Foo, args=(i,)) #串行
        #pool.apply_async(func=Foo, args=(i,)) #并行
    print("end")
    pool.close()
    pool.join()