#coding:utf-8

import time

"""
装饰器详解

import time

#高阶函数,把一个函数作为一个参数传递给另外一个函数调用，python中函数名也可以理解为变量名
def highlevel(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print "the function spent %s time" %(stop_time-start_time)

def foo():
    time.sleep(3)
    print "in the foo function"

highlevel(foo)

#嵌套函数
def grandpa():
    print "in the grandpa"
    def parent():
        print "in the parent"
        def son():
            print "in the son"
        son()
    parent()
grandpa()

#装饰器 = 高阶函数 + 嵌套函数
def deco(func):
    def warrper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print "the function spend %s time" %(stop_time-start_time)
    return warrper

@deco # 等同于bar = deco(bar)，其实bar已经变成了warpper
def bar():
    time.sleep(3)
    print "in the bar"

bar()

python3
#######################################################################################################################
import time

def highlevel(func):
    print(func)
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the function run time is %s" %(stop_time-start_time))

def foo():
    time.sleep(3)
    print("in the foo function")

def grander():
    print("in the grander")
    def parent():
        print("in the parent")
        def son():
            print("in the son")
        son()
    parent()
grander()

highlevel(foo)
#######################################################################################################################
def deco(func):
    def warrper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the function run time is %s" %(stop_time-start_time))
    return warrper

@deco
def bar():
    time.sleep(3)
    print("in the bar")

bar = deco(bar)
bar()
#######################################################################################################################
username = "james"
password = "nba"

def auth(auth_type):
    def outer_warpper(func):
        def warrper(*args, **kwargs):
            User = input ("please input your username ?")
            Pass = input ("please input your password ?")
            if auth_type == "local":
                if User == username and Pass == password:
                    res = func ()
                    print ("\033[032m welcome to you \033[0m")
                    return res
                else:
                    print ("\033[031m your username or password is worry \033[0m")
            elif auth_type == "ldap":
                print("it's not support ldap authentication")
        return warrper
    return outer_warpper


def index():
    print("this is index pager")

@auth(auth_type="local")
def home():
    print("this is home pager")
    return "home"

@auth(auth_type="ldap")
def data():
    print("this is data pager")
    return "data"

index()
rhome = home()
rdata = data()
print(rhome,rdata)
#######################################################################################################################

"""

##装饰器实际原理
########################################################################################################################
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
########################################################################################################################
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
########################################################################################################################
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
########################################################################################################################
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

########################################################################################################################
user = "james"
passwd = "nba123"

def auth(auth_type):
    def outter_warrper(func):
        def warrper(*args, **kwargs):
            Username = raw_input("please input username: ")
            Password = raw_input("please input password: ")
            if auth_type == "local":
                if user == Username and passwd == Password:
                    res = func(*args, **kwargs)
                    print "\033[32m authentication sucessful! \033[0m"
                    return res
                else:
                    print "\033[31m your username or password is wrong! \033[0m"
            elif auth_type == "ldap":
                print "\033[33m it's not support ldap auth,current! \033[0m"
        return warrper
    return outter_warrper


def index():
    print "welcome to index page"
    return "index"

@auth(auth_type="local")
def home():
    print "welcome to home page"
    return "home"

@auth(auth_type="ldap")
def data():
    print "welcome to data page"
    return "data"

retindex = index()
rethome = home()
retdata = data()
print(retindex,rethome,retdata)

##装饰器调用顺序
########################################################################################################################
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
########################################################################################################################
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