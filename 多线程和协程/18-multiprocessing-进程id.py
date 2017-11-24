#!/usr/bin/env python

import multiprocessing,os

def info(title):
    print(title)
    print("module name...",__name__)
    print("get parent process id",os.getppid())
    print("get process id",os.getpid())
    print("\n\n")

def f(name):
    info("called from child function f")
    print("hello",name)

if __name__  == "__main__":
    info("main process line")
    p = multiprocessing.Process(target=f,args=("bob",))
    p.start()