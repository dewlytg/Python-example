#coding:utf-8

import time

##装饰器实际原理
def deco(func):
    startTime = time.time()
    func()
    endTime = time.time()
    msecs = (endTime - startTime) * 1000
    print "-> elapsed time: %f ms" %msecs

def myfunc():
    print "start myfunc"
    time.sleep(0.6)
    print "end myfunc"

deco(myfunc)
myfunc()

##装饰器
def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print "-> elapsed time: %f ms" %msecs
    return wrapper

@deco
def myfunc():
    print "start myfunc"
    time.sleep(0.6)
    print "end myfunc"

myfunc()

##被装饰的函数带参数
def deco(func):
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime) * 1000
        print "-> elapsed time: %f ms" %msecs
    return wrapper

@deco
def addFunc(a,b):
    print "start addFunc"
    time.sleep(0.6)
    print "result is %d" %(a+b)
    print "end addFunc"

addFunc(3,8)

##带参数的装饰器
def deco(arg = True):
    if arg:
        def _deco(func):
            def warpper(*args,**kwargs):
                startTime = time.time()
                func(*args,**kwargs)
                endTime = time.time()
                msecs = (endTime - startTime) * 1000
                print "->elapsed time: %f ms" %msecs
            return warpper
    else:
        def _deco(func):
            return func
    return _deco

@deco(False)
def myFunc():
    print "start myFunc"
    time.sleep(0.6)
    print "end myFunc"

@deco(True)
def addFunc(a,b):
    print "start addFunc"
    time.sleep(0.6)
    print "result is %d" %(a+b)
    print "end addFunc"

print "myFunc is",myFunc.__name__
print
myFunc()
print "addFunc is",addFunc.__name__
addFunc(3,8)

##装饰器调用顺序
def deco_1(func):
    print "enter into deco_1"
    def wrapper(a,b):
        print "enter into deco_1_wrapper"
        func(a,b)
    return wrapper

def deco_2(func):
    print "enter into deco_2"
    def wrapper(a,b):
        print "enter into deco_2_wrapper"
        func(a,b)
    return wrapper

@deco_1
@deco_2
def addFunc(a,b):
    print "result is %d" %(a+b)

addFunc(3,8)

##Python内置装饰器
class Foo(object):
    def __init__(self,name):
        self.name = name

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self,var):
        self._var = var

foo = Foo("tom")
print foo.name
foo.var = "var1"
print foo.var