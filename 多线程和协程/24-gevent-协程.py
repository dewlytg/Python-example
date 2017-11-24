#!/usr/bin/env python

import gevent

def foo():
    print("Running in foo")
    gevent.sleep(2)
    print("Explicit context switch to foo again")

def bar():
    print("Explicit context to bar")
    gevent.sleep(1)
    print("Implicit context switch back to bar")

def func():
    print("running func")
    gevent.sleep(0)
    print("running func again")

gevent.joinall([
    gevent.spawn(foo), #生产一个协程
    gevent.spawn(bar),
    gevent.spawn(func)
]
)